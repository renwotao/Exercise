/*
    XSI memory shared
 */
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>
#include <string.h>
#include <sys/file.h>
#include <wait.h>
#include <sys/mman.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>

#define COUNT 100
#define PATHNAME "/etc/passwd"

int do_child(int proj_id)
{
    int interval;
    int *shm_p, shm_id;
    key_t shm_key;
    
    // call fork to generate shmkey
    if ((shm_key = ftok(PATHNAME, proj_id)) == -1) {
        perror("ftok()");
        exit(1);
    }

    // use shm_id in child process which was got from parent process
    shm_id = shmget(shm_key, sizeof(int), 0);
    if (shm_id < 0) {
        perror("shmget()");
        exit(1);
    }

    // shmat function maps shared memroy in local process 
    shm_p = (int *)shmat(shm_id, NULL, 0);
    if ((void *)shm_p == (void *)-1) {
        perror("shmat()");
        exit(1);
    }

    // critical section
    interval = *shm_p;
    interval++;
    usleep(1);
    *shm_p = interval;
    // critical section

    if (shmdt(shm_p) < 0) {
        perror("shmdt()");
        exit(1);
    }

    exit(0);
}

int main()
{
    pid_t pid;
    int count;
    int *shm_p;
    int shm_id, proj_id;
    key_t shm_key;

    proj_id = 1234;


    // use PATHNAME and proj_id to generate shm_key
    if ((shm_key = ftok(PATHNAME, proj_id)) == -1) {
        perror("ftok()");
        exit(1);
    }

    /* create a shared memory with shm_key and 
        set shared memory access permission 0666
    */
    shm_id = shmget(shm_key, sizeof(int), IPC_CREAT|IPC_EXCL|0600);
    if (shm_id < 0) {
        perror("shmget()");
        exit(1);
    }

    // attach shared memory to parent process
    shm_p = (int *)shmat(shm_id, NULL, 0);
    if ((void *)shm_p == (void *)-1) {
        perror("shmat()");
        exit(1);
    }

    *shm_p = 0;

    for (count = 0; count < COUNT; count++) {
        pid = fork();
        if (pid < 0) {
            perror("fork()");
            exit(1);
        }

        if (pid == 0) {
            do_child(proj_id);
        }
    }


    for (count = 0; count < COUNT; count++) {
        wait(NULL);
    }

    printf("shm_p: %d\n", *shm_p);

    // detach shared memory from parent process
    if (shmdt(shm_p) < 0) {
        perror("shmdt()");
        exit(1);
    }
    
    // delete shared memory
    if (shmctl(shm_id, IPC_RMID, NULL) < 0) {
        perror("shmctl()");
        exit(1);
    }

    exit(0);
}

