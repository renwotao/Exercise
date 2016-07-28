#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BUFSIZE 512

int main()
{
	int data_processed;
	int file_pipes[2];
	const char some_data[] = "123";
	char buffer[BUFSIZE + 1]; 
	pid_t fork_result;

	memset(buffer, '\0', sizeof(buffer));
	
	if (pipe(file_pipes) == 0) {
		fork_result = fork();
		if (fork_result == -1) {
			fprintf(stderr, "Fork failed");
			return -1;
		}	
		if (fork_result == 0) {
			close(0);
			dup(file_pipes[0]);
			close(file_pipes[0]);
			close(file_pipes[1]);
			
			execlp("od", "od", "-c", (char*)0);
			return 0;	
		} else {
			close(file_pipes[0]);
			data_processed = write(file_pipes[1], some_data, strlen(some_data));
			close(file_pipes[1]);
			printf("Wrote %d bytes\n", data_processed);
		}
	}

	return 0;
}
