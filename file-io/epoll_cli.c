#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <arpa/inet.h>

#define PORT 8787
#define IPADDRESS "127.0.0.1"
#define MAXSIZE 1024

int main()
{
    int clifd = socket(AF_INET, SOCK_STREAM, 0);
    if (clifd == -1) {
        perror("socket failed");
        return 1;
    }

    struct sockaddr_in srvaddr;
    srvaddr.sin_family = AF_INET;
    srvaddr.sin_port = htons(PORT);
    srvaddr.sin_addr.s_addr = inet_addr(IPADDRESS);

    int ret = connect(clifd, (struct sockaddr *)&srvaddr, sizeof(srvaddr));
    if (ret == -1) {
        perror("connect failed");
        return 1;
    }

    char sendbuf[] = "hello server";
    ret = send(clifd, sendbuf, sizeof(sendbuf), 0);
    if (ret == -1) {
        perror("send error");
        return 1;
    }
    char rcvbuf[MAXSIZE] = {'\0'};
    ret = recv(clifd, rcvbuf, sizeof(rcvbuf), 0);
    if (ret == -1) {
        perror("recv failed");
        return 1;
    }
    printf("receive message : %s\n", rcvbuf);
    
    return 0;
}
