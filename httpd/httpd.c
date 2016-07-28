#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <ctype.h>
#include <strings.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/wait.h>

#define ISspace(x) isspace((int)(x))

#define SERVER_STRING "Server: rwthttpd/0.1.0\r\n"

void accept_request(int);
void bad_request(int);
void cat(int, FILE *);
int get_line(int, char*, int);
void unimplemented(int);
void not_found(int);
void serve_file(int, const char *);
void execute_cgi(int, const char *, const char *, const char *); 
void cannot_execute(int);
/*
 * A request has caused a call to accept() on the server port 
 * to return. Process the request appropriately.
 * Parameters: the socket connected to the client
 */
 
void accept_request(int client)
{
	char buf[1024];
	int numchars;
	char method[255];
	char url[255];
	char path[512];
	size_t i, j;
	struct stat st;
	int cgi = 0;

	char *query_string = NULL;

	// get method from request line
	numchars = get_line(client, buf, sizeof(buf));
	i = 0; j = 0;
	while (!ISspace(buf[j]) && (i < sizeof(method) -1)) {
		method[i] = buf[j];
		i++; j++;
	}
	method[i] = '\0';
	
	// 不是 GET 或 POST 方法就告诉客户端没有实现
	if (strcasecmp(method, "GET") && strcasecmp(method, "POST"))
	{
		unimplemented(client);
		return;
	}
	
	// 如果是 POST 方法就将 cgi 标志变量置 1
	if (strcasecmp(method, "POST") == 0) {
		cgi = 1;
	}

	i = 0;
	// 跳过所有的空白字符（空格）
	while (ISspace(buf[j]) && (j < sizeof(buf)))
		j++;
	
	// 把 URL 读取出来放到 url 数组中
	while (!ISspace(buf[j]) && (i < sizeof(url) - 1) && (j < sizeof(buf)))
	{
		url[i] = buf[j];
		i++; j++;
	}
	url[i] = '\0';

	// 如果请求是一个 GET 方法的话
	if (strcasecmp(method, "GET") == 0) {
		query_string = url;
		
		// 跳过 ? 前的所有字符，遍历完也没有找到字符 ? 则退出循环
		while ((*query_string != '?') && (*query_string != '\0'))
			query_string++;

		if (*query_string == '?') {
			cgi = 1;
			
			*query_string = '\0';
		
			query_string++;
		}
	}

	// 
	sprintf(path, "htdocs%s", url);

	if (path[strlen(path) - 1] == '/')
		strcat(path, "index.html");
	
	
	if (stat(path, &st) == -1) {
		while ((numchars > 0) && strcmp("\n", buf))
			numchars = get_line(client, buf, sizeof(buf));

		not_found(client);
	} else {
		
		// 判断文件是文件夹则在path 后面拼接 "/index.html"
		if ((st.st_mode & S_IFMT) == S_IFDIR)
			strcat(path, "/index.html");
		
		// 如果这个文件是一个可执行文件，不论是属于用户/组/其他 这三者类型的，就将 cgi 标志置 1
		if ((st.st_mode & S_IXUSR)  ||
		    (st.st_mode & S_IXGRP)  ||
		    (st.st_mode & S_IXOTH)   )
			cgi = 1;

		if (!cgi)
			serve_file(client, path);
		else
			execute_cgi(client, path, method, query_string);
	}

	close(client);

}

void bad_request(int client)
{
	char buf[1024];
	
	sprintf(buf, "HTTP/1.0 400 BAD REQUEST\r\n");
	send(client, buf, sizeof(buf), 0);
	sprintf(buf, "Content-type: text/html\r\n");
	send(client, buf, sizeof(buf), 0);
	sprintf(buf, "\r\n");
	send(client, buf, sizeof(buf), 0);
	sprintf(buf, "<p>Your browser sent a bad request, ");
	send(client, buf, sizeof(buf), 0);
	sprintf(buf, "such as a POST without a Cotent-Length.\r\n");
	send(client, buf, sizeof(buf), 0);
}
/*Put the entire contents of a file out on a socket. This function
 * is named after the UNIX "cat" command, because it might have been
 * easier just to do something like pipe, fork and exec("cat").
 * Parameters: the client socket descriptor
 * 		FILE pointer for the file to cat
 *
 * */

void cat(int client, FILE *resource)
{
	char buf[1024];

	// 从文件中读取指定内容	
	fgets(buf, sizeof(buf), resource);
	while (!feof(resource)) {
		send(client, buf, strlen(buf), 0);
		fgets(buf, sizeof(buf), resource);
	}
}

/*Inform the client that a CGI script could not be executed.
 * Parameter: the client socket descriptor.
 * */
void cannot_execute(int client)
{
	char buf[1024];
	
	sprintf(buf, "HTTP/1.0 500 Internal Server Error\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "Content-type: text/html\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "<P>Error prohibited CGI execution.\r\n");
	send(client, buf, strlen(buf), 0);
}

/*Print out an error message with perror() and
 * exit the program indicating an error.
 * */
void error_die(const char *src)
{
	perror(src);
	exit(1);
}

void execute_cgi(int client, const char *path, 
		const char *method, const char *query_string)
{
	char buf[1024];
	int cgi_output[2];
	int cgi_input[2];
	pid_t pid;
	int status;
	int i;
	char c;
	int numchars = 1;
	int content_length = -1;

	buf[0] = 'A'; buf[1] = '\0';
	
	if (strcasecmp(method, "GET") == 0) {
		while ((numchars > 0) && strcmp("\n", buf))
			numchars = get_line(client, buf, sizeof(buf));
	} else {
		numchars = get_line(client, buf, sizeof(buf));

		while ((numchars > 0) && strcmp("\n", buf)) {
			buf[15] = '\0';
			if (strcasecmp(buf, "Content-Length:") == 0)
				content_length = atoi(&(buf[16]));
			numchars = get_line(client, buf, sizeof(buf));
		}

		if (content_length == -1) {
			bad_request(client);
			return;
		}
	}

	sprintf(buf, "HTTP/1.0 200 OK\r\n");
	send(client, buf, strlen(buf), 0);

	if (pipe(cgi_output) < 0) {
		cannot_execute(client);
		return;
	}
	if (pipe(cgi_input) < 0) {
		cannot_execute(client);
		return;
	}

	if ((pid = fork()) < 0) {
		cannot_execute(client);
		return;
	}

	if (pid == 0) {
		char meth_env[255];
		char query_env[255];
		char length_env[255];

		// 将子进程的 cgi_output 管道输出重定向到标准输出上
		dup2(cgi_output[1], 1);
		// 将子进程的 cgi_input 管道输入重定向到标准输出上
		dup2(cgi_input[0], 0);
		
		close(cgi_output[0]);
		close(cgi_input[1]);

		sprintf(meth_env, "REQUEST_METHOD=%s", method);
		// 将这个环境变量加进子进程的运行环境中
		putenv(meth_env);

		if (strcasecmp(method, "GET") == 0) {
			sprintf(query_env, "QUERY_STRING=%s", query_string);
			putenv(query_env);
		} else { // POST
			sprintf(length_env, "CONTENT_LENGTH=%d", content_length);
			putenv(length_env);
		}
		
		execl(path, path, NULL);
		exit(0);
	} else {
		close(cgi_output[1]);
		close(cgi_input[0]);

		if (strcasecmp(method, "POST") == 0) {
			for (i = 0; i < content_length; i++) {
				recv(client, &c, 1, 0);
				write(cgi_input[1], &c, 1);
			}
		}
		
		while (read(cgi_output[0], &c, 1) > 0) {
			send(client, &c, 1, 0);
		}

		close(cgi_output[0]);
		close(cgi_input[1]);

		waitpid(pid, &status, 0);	
	}
}

int get_line(int sock, char *buf, int size)
{
	int i = 0;
	char c = '\0';
	int n;

	while ((i < size - 1) && (c != '\n')) {
		n = recv(sock, &c, 1, 0);

		if (n > 0) {
			if (c == '\r') {
				n = recv(sock, &c, 1, MSG_PEEK);
				if ((n > 0) && (c == '\n'))
					recv(sock, &c, 1, 0);
				else
					c = '\n';
			}
			buf[i] = c;
			i++;
		} else 
			c = '\n';
	}
	buf[i] = '\0';

	return i;
}

/*Return the informational HTTP headers about a file.
 * Parameters: the socket to print the headers on
 * 		the name of the file.
 * */

void headers(int client, const char *filename)
{
	char buf[1024];
	(void)filename; // could use filename to determine file type

	strcpy(buf, "HTTP/1.0 200 OK\r\n");
	send(client, buf, strlen(buf), 0);
	strcpy(buf, SERVER_STRING);
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "Content-Type: text/html\r\n");
	send(client, buf, strlen(buf), 0);
	strcpy(buf, "\r\n");
	send(client, buf, strlen(buf), 0);

	
}

void not_found(int client)
{
	char buf[1024];

	sprintf(buf, "HTTP/1.0 404 NOT FOUND\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, SERVER_STRING);
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "Content-Type: text/html\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "<HTML><TITLE>Not Found</TITLE>\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "<BODY><P>The server could not fulfill\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "your request because the resource specified\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "is unavailable or nonexistent.\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "</BODY></HTML>\r\n");
	send(client, buf, strlen(buf), 0);	
}

/*Send a regular file to the client. Use headers, and report
 * errors to client if they occur.
 * Parameters: a pointer to a file structure produced from the 
 * 		socket file descriptor
 * 		the name of the file to serve
 * */
void serve_file(int client, const char *filename)
{
	FILE *resource = NULL;
	int numchars = 1;
	char buf[1024];

	buf[0] = 'A'; buf[1] = '\0';
	
	while ((numchars > 0) && strcmp("\n", buf)) 
		numchars = get_line(client, buf, sizeof(buf));
	
	resource = fopen(filename, "r");
	if (resource == NULL)
		not_found(client);
	else {
		headers(client, filename);
		
		cat(client, resource);
	}
	
	fclose(resource);
}

/*This function starts the process of listening for web connections
 * on a specified port. If the port is 0, then dynamically alllocate a
 * port and modify the original port variable to reflect the actual port.
 * Parameters: pointer to variable containing the port to connect on
 * Returns: the socket
 * */
int startup(u_short *port)
{
	int httpd = 0;
	struct sockaddr_in name;

	httpd = socket(PF_INET, SOCK_STREAM, 0);
	if (httpd == -1)
		error_die("socket");

	memset(&name, 0, sizeof(name));
	name.sin_family = AF_INET;
	name.sin_port = htons(*port);
	name.sin_addr.s_addr = htonl(INADDR_ANY);

	if (bind(httpd, (struct sockaddr *)&name, sizeof(name)) < 0)
		error_die("bind");

	if (*port == 0) {
		int namelen = sizeof(name);
		// 调用getsockanme()获取系统给 httpd 这个 socket 随机分配的端口号
		if (getsockname(httpd, (struct sockaddr *)&name, &namelen) == -1)
			error_die("getsockname");
		*port = ntohs(name.sin_port);
	}

	if (listen(httpd, 5) < 0)
		error_die("listen");
	
	return httpd;
}
/*Inform the client that the reqeusted web method has not been
 * implemented.
 * Parameter: the client socket
 * */
void unimplemented(int client)
{
	char buf[1024];
	
	sprintf(buf, "HTTP/1.0 501 Method Not Implemented\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, SERVER_STRING);
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "Content-Type: text/html\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "<HTML><HEAD><TITLE>Method Not Implemented\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "</TITLE></HEAD>\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "<BODY><P>HTTP request method not supported.\r\n");
	send(client, buf, strlen(buf), 0);
	sprintf(buf, "</BODY></HTML>\r\n");
	send(client, buf, strlen(buf), 0);
}

int main()
{
	int server_sock = -1;
	u_short port = 0;
	int client_sock = -1;
	
	struct sockaddr_in client_name;
	int client_name_len = sizeof(client_name);
	
	server_sock = startup(&port);
	printf("httpd running on port %d\n", port);

	while (1) 
	{
		client_sock = accept(server_sock,
					(struct sockaddr *)&client_name,
					&client_name_len);
		if (client_sock == -1)
			error_die("accept");
		accept_request(client_sock);
	}

	close(server_sock);

	return 0;
}
