#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define FILEPATH "/etc/passwd"
#define PROJID 1234
#define MSG "hello world!"

/* msgsnd 发送消息必须要使用自定义 msgbuf 结构体*/
struct msgbuf {
    long mtype;         // 类型参数
    char mtext[BUFSIZ]; // 消息体
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
    
    /* msgget 访问一个已经存在的消息队列时，msgflag 指定为 0 即可 */
    msgid = msgget(key, 0);
    if (msgid == -1) {
        perror("msgget");
        exit(1);
    }

    buf.mtype = 1;
    strncpy(buf.mtext, MSG, strlen(MSG));
    /* msgsnd 第三个参数为消息的长度而不是消息结构体的大小*/
    /* msgsnd 最后一个参数指定为 IPC_NOWAIT，
     在消息满的情况下，默认的发送行为会阻塞等待，
     如果加了这个参数，则不会阻塞，而是立即返回，并且errno设置为 EAGAIN*/
    if (msgsnd(msgid, &buf, strlen(buf.mtext), 0) == -1) {
        perror("msgsnd()");
        exit(1);
    }

    exit(0);
}
