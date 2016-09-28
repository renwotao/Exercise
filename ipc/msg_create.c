#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdlib.h>
#include <stdio.h>

#define FILEPATH "/etc/passwd"
#define PROJID 1234

int main()
{
    int msgid;
    key_t key;
    struct msqid_ds msg_buf;
    
    /* ftok 创建消息队列的标识*/
    key = ftok(FILEPATH, PROJID);
    if (key == -1) {
        perror("ftok()");
        exit(1);
    }
    
    /* 使用 IPC_PRIVATE 标识时，内核创建新的队列key不会与已存在队列冲突，
       此时msgflag应指定为IPC_CREAT*/
    /* 使用 IPC_CREATE | IPC_EXCL在制定key已经存在的情况下报错，
       而不是访问这个消息队列*/
    msgid = msgget(key, IPC_CREAT|IPC_EXCL|0600);
    if (msgid == -1) {
        perror("msgget()");
        exit(1);
    }

    if (msgctl(msgid, IPC_STAT, &msg_buf) == -1) {
        perror("msgctl");
        exit(1);
    }

    printf("msgid: %d\n", msgid);
    printf("msg_perm.uid: %d\n", msg_buf.msg_perm.uid);
    printf("msg_perm.gid: %d\n", msg_buf.msg_perm.gid);
    printf("msg_stime: %d\n", msg_buf.msg_stime);
    printf("msg_rtime: %d\n", msg_buf.msg_rtime);
    printf("msg_qnum: %d\n", msg_buf.msg_qnum);
    printf("msg_qbytes: %d\n", msg_buf.msg_qbytes);

    exit(0);
}
