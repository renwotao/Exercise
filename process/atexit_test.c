#include <stdio.h>
#include <stdlib.h>

/*
    atexit() 正常测
 */

void out()
{
    printf("atexit() succeeded!\n");
}

int main()
{
    if (atexit(out))
        perror("atexit() failed!\n");

    return 0;
}
