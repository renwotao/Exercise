#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>

/*
    ----------
    | socket |
    ----------
        |
        |
     --------    sockaddr_in{}
     | bind | <---  本机
     --------
        |
        |
    ----------
    | listen |
    ----------
        |
        |
    ----------   sockaddr_in{}
    | accept | ---> 对等实体
    ----------
        |
        |
     --------
     | recv |
     | send |
     --------
*/

int main()
{
    struct sockaddr_in local;
    int s;
    int s1;
    int rc;
    char buf[1];

    local.sin_family = AF_INET;  // 物理层、链路层协议
    local.sin_port = htons(7500);  // 传输层端口
    local.sin_addr.s_addr = htonl(INADDR_ANY);  // IP层（网络层）IP地址
    s = socket(AF_INET, SOCK_STREAM, 0);  // SOCK_STREAM 定义传输层选择的协议，这里选择TCP
    if (s < 0) {
        perror("socket call failed");
        exit(1);
    }
    rc = bind(s, (struct sockaddr *)&local, sizeof(local));
    if (rc < 0) {
        perror("bind call failed");
        exit(1);
    }
    /* 
       listen 函数的作用就是把套接字标识为监听状态,并放入内核监听列表。
       当主机收到一个连接请求时，内核会搜索监听套接字列表，
       查找与连接请求中目的地址呵端口号相匹配的那个套接字。
     
       int listen(SOCKET s, int backlog);
       参数backlog是挂起连接的最大数量，
       它并不是在指定端口上同时可建立连接的最大值，
       而是排队等待应用程序接受的连接或部分连接的最大数量。

       现在backlog值的设置与系统有关，可根据系统文档设置。
     */
    rc = listen(s, 5);
    if (rc < 0) {
        perror("listen call failed");
        exit(1);
    }
    s1 = accept(s, NULL, NULL);
    if (s1 < 0) {
        perror("accept call failed");
        exit(1);
    }
    rc = recv(s1, buf, 1, 0);
    if (rc <= 0) {
        perror("recv call failed");
        exit(1);
    }
    printf("%c\n", buf[0]);
    rc = send(s1, "2", 1, 0);
    if (rc <= 0) {
        perror("send call failed");
    }
    exit(1);
}
