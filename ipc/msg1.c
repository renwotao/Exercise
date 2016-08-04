#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/msg.h>

#define BUFSZ 512

struct my_msg_st {
	long int my_msg_type;
	char some_text[BUFSZ];
};

int main()
{
	int running = 1;
	int msgid;
	struct my_msg_st some_data;
	long int msg_to_receive = 0;

	msgid = msgget((key_t)1234, 0666|IPC_CREAT);
	if (msgid == -1) {
		fprintf(stderr, "msgget failed with error: %d\n", errno);
		exit(-1);
	}

	while (running) {
		if (msgrcv(msgid, (void *)&some_data, BUFSZ,
			msg_to_receive, 0) == -1) {
			fprintf(stderr, "msgrcv failed with error: %d\n", errno);
			exit(-1);
		}
		printf("You wrote: %s", some_data.some_text);
		if (strncmp(some_data.some_text, "end", 3) == 0) {
			running = 0;
		}

	}
	if (msgctl(msgid, IPC_RMID, 0) == -1) {
		fprintf(stderr, "msgctl(IPC_RMID) failed\n");
		exit(-1);
	}
		
	exit(0);
}
