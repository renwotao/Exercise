
void read_file(int fd, char buf[], int len)
{
	ssize_t ret;
	while (len != 0 && (ret = read(fd, buf, len)) != 0) {
		if (ret == -1) {
			if (errno == EINIR)
				continue;
			perror("read");
			break;
		}
		
		len -= ret;
		buf += ret;
	}
}
