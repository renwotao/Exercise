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
	
	memset(buffer, '\0', sizeof(buffer));
	
	if (pipe(file_pipes) == 0) {
		data_processed = write(file_pipes[1], some_data, strlen(some_data));
		printf("Wrote %d bytes\n", data_processed);
		data_processed = read(file_pipes[0], buffer, BUFSIZE);
		printf("Read %d bytes: %s\n", data_processed, buffer);
	}

	return 0;
}
