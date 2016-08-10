/*
    mySleep.c
 */
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

void mySleep(long sec, long usec) 
{
    struct timeval tv;
    tv.tv_sec = sec;
    tv.tv_usec = usec;

    select(0, NULL, NULL, NULL, &tv);
}
