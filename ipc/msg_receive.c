#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define FILEPATH "/etc/passwd"
#define PROJID 1234

struct msgbuf {
    long mtype;
    char mtext[BUFSIZ];
};
int main()
{
    int msgid;
    key_t key;
    struct msgbuf buf;

    key = ftok(FILEPATH, PROJID);
    if (key == -1) {
        perror("ftok()");
        exit(1);
    }
    
    /* msgrcv 会将消息从指定队列中删除 */
    /* 第三个参数指定消息的buf长度，如果消息内容长度大于指定的长度，
     那么函数的行为将取决于最后一个参数mssgflag是否设置了 MSG_NOERROR, 
     如果这个标识被设定，消息将被截短，消息剩余部分将会被丢失。
     如果没有设置这个标识，msgrcv 会失败返回，errno被设定为 E2BIG */

    /* 最后一个参数可以设置为 IPC_NOWAIT，非阻塞方式读取。
     当队列为空的时候，msgrcv 会阻塞等待。
     加这个标识后将直接返回，errno被设置为 ENOMSG*/
    if (msgrcv(msgid, &buf, BUFSIZ, 1, 0) == -1) {
        perror("msgrcv()");
        exit(1);
    }

    printf("mtype: %d\n", buf.mtype);
    printf("mtype: %s\n", buf.mtext);

    if (msgctl(msgid, IPC_RMID, NULL) == -1) {
        perror("msgctl()");
        exit(1);
    }

    exit(0);
}
