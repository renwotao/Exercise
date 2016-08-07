#ifndef _READ_FILE_
#define _READ_FILE_
/*	function:
		read_file: read content from file and put it in buffer
 	parameters:
		fd	: file descriptor
		buf[]	: buffer file content
		len 	: file size 	
*/
void read_file(int fd, char buf[], int len);

#endif
