#include <ctype.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

#define BSZ 4096

unsigned char buf[BSZ];

unsigned char translate(unsigned char c) 
{
    if (isalpha(c)) {
        if (c >= 'n') {
            c -= 13;
        } else if (c >= 'a') {
            c += 13;
        } else if (c >= 'N') {
            c -= 13;
        } else {
            c += 13;
        }
    }

    return c;
}

int main(int argc, char *argv[])
{
    int ifd, ofd, i, n, nw;

    if (argc != 3) {
        puts("usage: rot13 infile outfile");
        return 1;
    }

    if ((ifd = open(argv[1], O_RDONLY)) < 0) {
        printf("can't open %s\n", argv[1]);
        return 1;
    }

    if ((ofd = open(argv[2], O_RDWR|O_CREAT|O_TRUNC, 0644)) < 0) {
        printf("can't create %s\n", argv[2]);
        return 1;
    }

    while ((n = read(ifd, buf, BSZ)) > 0) {
        for (i = 0; i < n; i++)
            buf[i] = translate(buf[i]);
        if ((nw = write(ofd, buf, n)) != n) {
            if (nw < 0) {
                perror("write failed");
                return 1;
            } else {
                printf("short write (%d/%d)\n", nw, n);
                return 1;
            }
        }
    }
    fsync(ofd);
    
    return 0;
}
