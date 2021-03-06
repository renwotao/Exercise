#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/shm.h>
#include "shm_com.h"

int main()
{
	int running = 1;
	void *shared_memory = (void*) 0;
	struct shared_use_st *shared_stuff;
	int shmid;

	srand((unsigned int)getpid());
	
	// get shared memory id
	shmid = shmget((key_t)1234, sizeof(struct shared_use_st), 0666|IPC_CREAT);
	if (shmid == -1) {
		perror("shmget failed\n");
		exit(-1);
	}
	
	// attach
	shared_memory = shmat(shmid, (void*)0, 0);
	if (shared_memory == (void *)-1) {
		perror("shmat failed\n");
		exit(-1);
	}

	printf("Memory attached at %X\n", (int)shared_memory);

	shared_stuff = (struct shared_use_st *)shared_memory;
	shared_stuff->written_by_you = 0;
	while (running) {
		if (shared_stuff->written_by_you) {
			printf("You wrote: %s", shared_stuff->some_text);
			sleep( rand() % 4);
			shared_stuff->written_by_you = 0;
			if (strncmp(shared_stuff->some_text, "end", 3) == 0) {
				running = 0;
			}
		}
	}
	
	// detach
	if (shmdt(shared_memory) == -1) {
		perror("shmdt failed\n");
		exit(-1);
	}
	
	// delete 
	if (shmctl(shmid, IPC_RMID, 0) == -1) {
		perror("shmctl(IPC_RMID) failed\n");
		exit(-1);
	}

	exit(0);
}
