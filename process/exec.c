#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>

char *env_init[] = { "USER=unknown", "PATH=/tmp", NULL };

int main()
{
    extern char **environ;
    char **ptr;
    for (ptr = environ; *ptr != 0; ptr++)
        printf("%s\n", *ptr);
    
    pid_t pid;

    if ((pid = fork()) < 0) {
        perror("fork error");
        return 1;
    } else if (pid == 0) {
        // execle(const char *path, const char *arg0, ..., (char *)0);
        if (execle("/home/renhai/workspace/exercise/process/echoall", 
                    "echoall", "myarg1", "MY ARG2", (char *)0, 
                    env_init) < 0) {
            perror("execle error");
            return 1;
        }
    }

    if (waitpid(pid, NULL, 0) < 0) {
        perror("wait error");
        return 1;
    }

    if ((pid = fork()) < 0) {
        perror("fork error");
        return 1;
    } else if (pid == 0) {
        // search "echoall" from PATH which inherit from parent process
        // execlp(const char *filename, const char *arg0, ..., (char *)0);
        if (execlp("echoall", "echoall", "only 1 arg", (char *) 0) < 0) {
            perror("execlp error");
            return 1;
        }
    }

    return 0;
}
