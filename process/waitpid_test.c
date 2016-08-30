#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    int status;
    pid_t pid;

    pid = fork();
    if (pid == -1)
        return 1;
    else if (pid > 0) {

        pid = waitpid(pid, &status, WNOHANG);
        if (pid == -1)
            perror("waitpid");
        else { 
            printf("pid=%d\n", pid);

            if (WIFEXITED(status))
                printf("Normal termination with exit status=%d\n",
                        WEXITSTATUS(status));

            if (WIFSIGNALED(status))
                printf("Killed by signal=%d%s\n",
                        WTERMSIG(status),
                        WCOREDUMP(status) ? " (dumped core)" : "");
        }    
    }
    return 0;
}
