#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <linux/limits.h>

int main()
{
    pid_t pid;
    int i;

    /* create new process */
    pid = fork();
    if (pid == -1)  
        return -1;
    else if (pid != 0) 
        exit(0);

    /* create new session and process group */
    if (setsid() == -1)
        return -1;

    /* set the working directory to the root directory */
    if (chdir("/") == -1) 
        return -1;

    /* close all open files --NR_OPEN is overkill, but works */
    for (int i = 0; i < NR_OPEN; i++) 
        close(i);

    /* redirect fd's 0, 1, 2 to /dev/null */
    open("/dev/null", O_RDWR); /* stdin */
    dup(0);                    /* stdout */
    dup(0);                    /* stderror */

    /* do its daemon thing... */
    return 0;
}
