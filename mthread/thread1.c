#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>

void *thread_function(void *arg);
sem_t bin_sem;

#define WORK_SIZE 1024
char work_area[WORK_SIZE];

int main()
{
	int res;
	pthread_t a_thread;
	void *thread_result;

	res = sem_init(&bin_sem, 0, 0);
	if (res != 0) {
		perror("Semaphore initalization failed");
		exit(-1);
	}

	res = pthread_create(&a_thread, NULL, thread_function, NULL);
	if (res != 0) {
		perror("Thread creation failed");
		exit(-1);
	}
	
	printf("Input some text. Enter 'end' to finish\n");
	while (strncmp("end", work_area, 3) != 0) {
		if (strncmp(work_area, "FAST", 4) == 0) {
			sem_post(&bin_sem);
			printf("send sem-\n");
			strcpy(work_area, "Wheeee...");
		} else {
			fgets(work_area, WORK_SIZE, stdin);
		}
		// send semaphore
		sem_post(&bin_sem);
		printf("send sem--\n");
	}	

	printf("\nWaiting for thread to finish...\n");
	res = pthread_join(a_thread, &thread_result);
	if (res != 0) {
		perror("Thread join failed");
		exit(-1);
	}

	printf("Thread joined\n");
	sem_destroy(&bin_sem);
	exit(0);
	

}

void *thread_function(void *arg) 
{
	// recv semaphore
	sem_wait(&bin_sem);
	while (strncmp("end", work_area, 3) != 0) {
		printf("You input %d charactors\n", strlen(work_area)-1);
		sem_wait(&bin_sem);
	}
	pthread_exit(NULL);
}
