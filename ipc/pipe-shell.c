#include <unistd.h>
#include <stdio.h>
#include <stdio.h>
#include <string.h>

#define BUFSIZE 512
int main()
{
	FILE *read_fp;
	char buffer[BUFSIZE + 1];
	int chars_read;
	
	memset(buffer, '\0', sizeof(buffer));
	read_fp = popen("cat pipe*.c |wc -l", "r");
	if (read_fp != NULL) {
		chars_read = fread(buffer, sizeof(char), BUFSIZE, read_fp);
		printf("Reading:-\n %s\n", buffer);
		chars_read = fread(buffer, sizeof(char), BUFSIZE, read_fp);
	}
	pclose(read_fp);
	
	return 0;
}
