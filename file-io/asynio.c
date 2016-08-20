#include <string.h>
#include <ctype.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <error.h>
#include <aio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>

#define BSZ 4096
#define NBUF 8

enum rwop {
    UNUSED = 0,
    READ_PENDING = 1,
    WRITE_PENDING = 2
};

struct buf {
    enum rwop op;
    int last;
    struct aiocb aiocb;
    unsigned char data[BSZ];
};

struct buf bufs[NBUF];

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
    int ifd, ofd, i, j, n, err, numop;
    struct stat sbuf;
    const struct aiocb *aiolist[NBUF];
    off_t off = 0;

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
    
    if (fstat(ifd, &sbuf) < 0) {
        perror("fstat failed");
        return 1;
    }
    

    for (i = 0; i < NBUF; i++) {
        bufs[i].op = UNUSED;
        bufs[i].aiocb.aio_buf = bufs[i].data;
        bufs[i].aiocb.aio_sigevent.sigev_notify = SIGEV_NONE;
        aiolist[i] = NULL;
    }

    numop = 0;
    for (;;) {
        for (i = 0; i < NBUF; i++) {
            switch (bufs[i].op) {
            /*
              Read from the input file if more data remains unread.
             */    
                case UNUSED:
                        if (off < sbuf.st_size) {
                            bufs[i].op = READ_PENDING;
                            bufs[i].aiocb.aio_fildes = ifd;
                            bufs[i].aiocb.aio_offset = off;
                            off += BSZ;
                            if (off >= sbuf.st_size)
                                    bufs[i].last = 1;
                            bufs[i].aiocb.aio_nbytes = BSZ;
                            if (aio_read(&bufs[i].aiocb) < 0) {
                                perror("aio_read failed");
                                return 1;
                            }
                            aiolist[i] = &bufs[i].aiocb;
                            numop++;
                        }
                        break;
                case READ_PENDING:
                        if ((err = aio_error(&bufs[i].aiocb)) == EINPROGRESS)
                            continue;
                        if (err != 0) {
                            if (err == -1) {
                                perror("aio_error failed");
                                return 1;
                            } else {
                                printf("read failed %s\n", strerror(err));
                                return 1;
                            }
                        }
                        /*
                            A read is complete; translate the buffer and write it
                         */

                        if ((n = aio_return(&bufs[i].aiocb)) < 0) {
                            perror("aio_return failed");
                            return 1;
                        }
                        if (n != BSZ && !bufs[i].last) {
                            printf("short read (%d/%d)\n", n, BSZ);
                            return 1;
                        }
                        for (j = 0; j < n; j++) 
                            bufs[i].data[j] = translate(bufs[i].data[j]);
                        bufs[i].op = WRITE_PENDING;
                        bufs[i].aiocb.aio_fildes = ofd;
                        bufs[i].aiocb.aio_nbytes = n;
                        if (aio_write(&bufs[i].aiocb) < 0) {
                            perror("aio_write failed");
                            return 1;
                        }
                        break;
                case WRITE_PENDING:
                        if ((err = aio_error(&bufs[i].aiocb)) == EINPROGRESS)
                            continue;
                        if (err != 0) {
                            if (err == -1) {
                                perror("aio_error failed");
                                return 1;
                            } else {
                                printf("write failed  %s\n", strerror(err));
                            }
                        }

                        if ((n = aio_return(&bufs[i].aiocb)) < 0) {
                            perror("aio_return failed");
                            return 1;
                        }
                        if (n != bufs[i].aiocb.aio_nbytes) {
                            printf("short write (%d/%d)\n", n, BSZ);
                            return 1;
                        }
                        aiolist[i] = NULL;
                        bufs[i].op = UNUSED;
                        numop--;
                        break;

            }
        
        }

        if (numop == 0) {
            if (off >= sbuf.st_size)
                break;
        } else {
            if (aio_suspend(aiolist, NBUF, NULL) < 0) {
                perror("aio_suspend failed");
                return 1;
            }
        }

    }

    bufs[0].aiocb.aio_fildes = ofd;
    if (aio_fsync(O_SYNC, &bufs[0].aiocb) < 0) {
        perror("aio_fsync failed");
        return 1;
    }

    return 0;
}
