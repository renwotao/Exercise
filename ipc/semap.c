#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/sem.h>
#include "semap.h"

static int set_semvalue();
static void del_semvalue();
static int semaphore_p();
static int semaphore_v();

static int sem_id;

int main(int argc, char *argv[])
{
	int i ;
	int pause_time;
	char op_char = 'O';
	
	srand((unsigned int)getpid());
	
	sem_id = semget((key_t)1234, 1, 0666|IPC_CREAT);
	if (argc > 1) {
		if (!set_semvalue()) {
			perror("Failed to initialize semphore\n");
			exit(-1);
		}
		op_char = 'X';
		sleep(2);
	}

	for (i = 0; i < 10; i++) {
		if (!semaphore_p()) 
			exit(-1);
		printf("%c", op_char);
		fflush(stdout);
		pause_time = rand()%3;
		sleep(pause_time);
		printf("%c", op_char);
		fflush(stdout);

		if (!semaphore_v())
			exit(-1);
		pause_time = rand() %2;
		sleep(pause_time);
	}

	printf("\n%d = finished\n", getpid());
	
	if (argc > 1) {
		sleep(10);
		del_semvalue();
	}
	exit(0);
}


static int set_semvalue()
{
	union semun sem_union;
	
	sem_union.val = 1;
	if (semctl(sem_id, 0, SETVAL, sem_union) == -1)
		return 0;
	return 1;
}

static int semaphore_p()
{
	struct sembuf sem_b;
	
	sem_b.sem_num = 0;
	sem_b.sem_op = -1; 
	sem_b.sem_flg = SEM_UNDO;
	if (semop(sem_id, &sem_b, 1) == -1) {
		perror("semaphore_p failed\n");
		return 0;
	}
	return 1;
}

static int semaphore_v()
{
	struct sembuf sem_b;

	sem_b.sem_num = 0;
	sem_b.sem_op = 1; 
	sem_b.sem_flg = SEM_UNDO;
	if (semop(sem_id, &sem_b, 1) == -1) {
		perror("semaphore_v failed\n");
		return 0;
	}
	return 1;
}

static void del_semvalue()
{
	union semun sem_union;
	
	if (semctl(sem_id, 0, IPC_RMID, sem_union) == -1) {
		perror("Failed to delete semaphore\n");
	}
}
