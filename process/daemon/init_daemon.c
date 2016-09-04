#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/param.h>
#include <sys/types.h>
#include <sys/stat.h>

void init_daemon()
{
    pid_t pid;
    int i;

    /* 处理　SIGCHLD 信号。*/
    /* 处理　SIGCHLD 信号并不是必须的。但对于某些进程，别是服务器进程在请求到来是生成子进程处理请求。
     　如果父进程不等待子进程结束，子进程将成为僵尸进程( zombie ) 从而占用系统资源。　
     */
    if (signal(SIGCHLD, SIG_IGN) == SIG_ERR) {
        perror("Cannot signal in init_daemon.");
        exit(1);
    }
    
    if (pid = fork()) 
        exit(0);
    else if (pid < 0) {
        perror("failed to fork1");
        exit(1);
    }

    /* 第一子进程，后台继续执行　*/
    setsid(); /* 第一子进程成为新的会话首进程　*/
    
    /* 与控制端分离*/
    if (pid = fork())
        exit(0);
    else if (pid < 0) 
        exit(1); /* fork 失败，退出　*/

    /* 第二子进程，继续　*/
    /* 第二子进程不再是会话首进程,禁止进程重新打开控制端　*/

    for (i = 0; i < getdtablesize(); ++i) 
        close(i); /* 关闭打开的文件描述符　*/
    chdir("/tmp");/* 改变工作目录到　/tmp */
    umask(0);     /* 重设文件创建掩码　*/

    return;
}
