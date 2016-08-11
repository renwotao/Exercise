#include <sys/epoll.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>

#define PORT 8787
#define MAXSIZE 1024
#define LISTENQ 5
// #define FDSIZE 1000
#define EPOLLEVENTS 100


// add event
static void add_event(int epollfd, int fd, int state)
{
    struct epoll_event ev;
    ev.events = state;
    ev.data.fd = fd;
    epoll_ctl(epollfd, EPOLL_CTL_ADD, fd, &ev);
}

/*
    notice:
           call close() to close fd after call  epoll_ctl to delete fd from epoll
           if not, will error Bad file descriptor
 */
// delete event
static void delete_event(int epollfd, int fd, int state)
{
    struct epoll_event ev;
    ev.events = state;
    ev.data.fd = fd;
    epoll_ctl(epollfd, EPOLL_CTL_DEL, fd, &ev);
}

// modify event
static void modify_event(int epollfd, int fd, int state)
{
    struct epoll_event ev;
    ev.events = state;
    ev.data.fd = fd;
    epoll_ctl(epollfd, EPOLL_CTL_MOD, fd, &ev);
}

// handle accept
static void handle_accept(int epollfd, int listenfd) 
{
    int clifd;
    struct sockaddr_in cliaddr;
    socklen_t cliaddrlen;
    /*
        notice: clear cliaddr struct every accept.
        if not, will error Invalid argument 
    */
    memset(&cliaddr, 0, sizeof(cliaddr));

    clifd = accept(listenfd, (struct sockaddr*)&cliaddr, &cliaddrlen);
    if (clifd == -1) 
            perror("accept error");
    else {
        printf("accept a new client: %s:%d\n", inet_ntoa(cliaddr.sin_addr),
                cliaddr.sin_port);
        add_event(epollfd, clifd, EPOLLIN);
    }
}


// handle read
static void do_read(int epollfd, int fd, char *buf) 
{
    int nread;
    nread = read(fd, buf, MAXSIZE);
    if (nread == -1) {
        perror("read error");
        delete_event(epollfd, fd, EPOLLIN);
        close(fd);
    } else if (nread == 0) {
        perror("client close");
        delete_event(epollfd, fd, EPOLLIN);
        close(fd);
    } else {
        printf("read message is : %s\n", buf);
        modify_event(epollfd, fd, EPOLLOUT);
    }
}

// handle write
static void do_write(int epollfd, int fd, char *buf) 
{
    int nwrite;
    nwrite = write(fd, buf, strlen(buf));
    if (nwrite == -1) {
        perror("write error");
        delete_event(epollfd, fd, EPOLLOUT);
        close(fd);
    } else {
        modify_event(epollfd, fd, EPOLLIN);
    }
    memset(buf, 0, MAXSIZE);
}

// handle events
static void handle_events(int epollfd, struct epoll_event *events, 
        int num, int listenfd, char *buf) {
    int i;
    int fd;
    for (int i = 0; i < num; i++) {
        fd = events[i].data.fd;
        if (fd == listenfd && events[i].events & EPOLLIN) 
                handle_accept(epollfd, listenfd);
        else if (events[i].events & EPOLLIN)
                do_read(epollfd, fd, buf);
        else if (events[i].events & EPOLLOUT) {
                strcpy(buf, "hello client");                                
                do_write(epollfd, fd, buf);
        }
    }
}

int main()
{
    char buf[MAXSIZE];
    int listenfd;
    struct sockaddr_in srvaddr;
    
    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    if (listenfd == -1) {
        perror("socket failed");
        return -1;
    }
    
    srvaddr.sin_family = AF_INET;
    srvaddr.sin_port = htons(PORT);
    srvaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    // bind
    if (bind(listenfd, (struct sockaddr *)&srvaddr, sizeof(srvaddr)) == -1) {
        perror("bind failed");
        return -1;
    }
    // listen
    if (listen(listenfd, LISTENQ) == -1) {
        perror("listen failed");
        return -1;
    }

    // create epoll context
    struct epoll_event events[EPOLLEVENTS];

    int epollfd = epoll_create1(0);
    if (epollfd == -1) {
        perror("epoll create1");
        return -1;
    }

    struct epoll_event ev;
    ev.events = EPOLLIN;
    ev.data.fd = listenfd;
    if (epoll_ctl(epollfd, EPOLL_CTL_ADD, listenfd, &ev) == -1) {
       perror("epoll_ctl: listenfd");
       return -1;
    }

    for (;;) {
        int ret = epoll_wait(epollfd, events, EPOLLEVENTS, -1);
        if (ret == -1) {
            perror("epoll wait");
            return -1;
        }

        handle_events(epollfd, events, ret, listenfd, buf);
    }

}
