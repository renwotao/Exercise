#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/sem.h>
#include <signal.h>

#define START 10010001
#define END 10020000
#define NPROC 4

static int pvid;

int mysem_init()
{
    int semid;
    
    semid = semget(IPC_PRIVATE, 1, IPC_CREAT|0600);
    if (semid < 0) {
        perror("semget()");
        return -1;
    }
    if (semctl(semid, 0, SETVAL, 1) < 0) {
        perror("semctl()");
        return -1;
    }
    return semid;
}

void mysem_destroy(int lockid)
{
    semctl(lockid, 0, IPC_RMID);
}

int P(int lockid)
{
    struct sembuf sbuf;

    sbuf.sem_num = 0;
    sbuf.sem_op = -1;
    sbuf.sem_flg = 0;

    while (semop(lockid, &sbuf, 1) < 0) {
        if (errno == EINTR) {
            continue;
        }
        perror("sempop()");
        return -1;
    }

    return 0;
}

int V(int lockid)
{
    struct sembuf sbuf;

    sbuf.sem_num = 0;
    sbuf.sem_op = 1;
    sbuf.sem_flg = 0;

    if (semop(lockid, &sbuf, 1) < 0) {
        perror("semop()");
        return -1;
    }

    return 0;
}

int prime_proc(int n)
{
    int i, j, flag;

    flag = 1;
    for (i = 2; i < n/2; ++i) {
        if (n%i == 0) {
            flag = 0;
            break;
        }
    }

    if (flag == 1) {
        printf("%d is a prime\n", n);
    }

    /* 子进程判断完成当前数字退出之前进行V操作 */
    V(pvid);
    exit(0);
}

void sig_child(int sig_num)
{
    while (waitpid(-1, NULL, WNOHANG) > 0);
}
    

int main()
{
    pid_t pid;
    int i;
    
    /* 当子进程退出的时候使用信号处理进行回收，以防止产生很多僵尸进程 */
    if (signal(SIGCHLD, sig_child) == SIG_ERR) {
        perror("signal()");
        exit(1);
    }

    pvid = mysem_init(NPROC);
    
    /* 每个要运算的数字都打开一个子进程进行判断 */
    for (i = START; i < END; i+=2) {
        /* 创建子进程的时候进行P操作 */
        P(pvid);
        pid = fork();
        if (pid < 0) {
            /* 创建失败则应该V操作 */
            V(pvid);
            perror("fork()");
            exit(1);
        }

        if (pid == 0) {
            /* 创建子进程进行这个数字的判断 */
            prime_proc(i);
        }
    }


    /* 在此等待所有数都运算完，以防止运算到最后父进程先mysem_destroy, 导致最后四个子进程进行V操作时报错 */
    while (1) { sleep(1); }
    mysem_destroy(pvid);
    
    exit(0);
}

