#include <pthread.h>
#include <mqueue.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/*
  mq_notify 的行为：
 1 一个消息队列只能通过 mq_notify 注册一个进程进行异步处理。
 2 异步通知只会在消息队列从空变成非空的时候产生，其他队列的变动不会触发异步通知。
 3 如果其他进程使用 mq_receive 等待队列的消息时，
 消息到来不会触发已注册 mq_notify 的程序产生异步通知。
 队列的消息会递送给在使用 mq_receive 等待的进程。
 4 一次 mq_notify 注册只会触发一次异步事件，伺候如果队列在此由空变为非空也不会触发异步通知。
 如果需要一直可以触发，请处理异步通知后再次注册 mq_notify。
 5 如果 sevp 指定为 NULL，表示取消注册异步通知。
    
 */

#define handle_error(msg) \
    do { perror(msg); exit(EXIT_FAILURE); } while (0)

static void tfunc(union sigval sv) 
{
    /* 此函数在队列变为非空的时候会被触发执行 */

    struct mq_attr attr;
    ssize_t nr;
    void *buf;

    /* 使用 sigval_ptr 指针传递此变量的值 */
    mqd_t mqdes = *((mqd_t *) sv.sival_ptr);

    /* Determine max. msg size, allocate buffer to receive msg */

    if (mq_getattr(mqdes, &attr) == -1)
        handle_error("mq_getattr");
    
    buf = malloc(attr.mq_msgsize);
    if (buf == NULL) 
        handle_error("malloc");

    /* 打印队列中相关消息信息 */
    nr = mq_receive(mqdes, buf, attr.mq_msgsize, NULL);
    if (nr == -1) 
        handle_error("mq_receive");

    printf("Read %zd bytes from MQ\n", nr);
    free(buf);

    /* 本程序取到消息之后直接退出，不会循环处理 */
    exit(EXIT_SUCCESS);  /* Terminate the process */
}

int main(int argc, char *argv[]) 
{
    mqd_t mqdes;
    struct sigevent sev;

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <mq-name>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    mqdes = mq_open(argv[1], O_RDONLY);
    if (mqdes == (mqd_t) -1) 
        handle_error("mq_open");

    /* 在此指定当异步事件来的时候以线程方式处理，
     触发的线程： tfunc
     线程属性设置为： NULL
     需要给线程传递消息队列描述付mqdes，以便线程接收消息 */

    sev.sigev_notify = SIGEV_THREAD;
    sev.sigev_notify_function = tfunc;
    sev.sigev_notify_attributes = NULL;
    sev.sigev_value.sival_ptr = &mqdes; /* Arg to thread func */

    if (mq_notify(mqdes, &sev) == -1) 
        handle_error("mq_notify");

    pause(); 
}
