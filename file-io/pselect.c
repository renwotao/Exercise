#include <sys/select.h>
#include <sys/time.h>
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

#define MAXLINE 255

void sig_alarm(int signo)
{
    if (signo == SIGALRM) {
        printf("SIGALRM\n");
    }
}

int main()
{
    sigset_t sigmask;
    fd_set rset;
    ssize_t nread;
    char buf[MAXLINE] = {'\0'};
    int maxfd;
   
    struct itimerval value;
    value.it_interval.tv_sec = 3;
    value.it_interval.tv_usec = 0;
    value.it_value.tv_sec = 1;
    value.it_value.tv_usec = 0;
    
    signal(SIGALRM, sig_alarm);

    if (setitimer(ITIMER_REAL, &value, NULL) == -1) {
        perror("setitimer error");
        return 1;
    }

    // mask alarm signal when call pselect
    if (sigemptyset(&sigmask) == -1) {
        perror("sigemptyset error");
        return 1;
    }
    if (sigaddset(&sigmask, SIGALRM) == -1) {
        perror("sigaddset error");
        return 1;
    }
    
    while (1) {
        FD_ZERO(&rset);
        FD_SET(fileno(stdin), &rset);
        maxfd = fileno(stdin) + 1;
        memset(buf, 0, sizeof(buf));
        
        int nready = pselect(maxfd, &rset, NULL, NULL, NULL, &sigmask);
        if (nready < 0) {
            if (errno == EINTR) {
                perror("interrupt");
            }
        } else {
            int nread = read(fileno(stdin), buf, MAXLINE);
            if (nread < 0) {
                perror("read failed");
                continue;
            }

            printf("%s\n", buf);
        }
    }
}
