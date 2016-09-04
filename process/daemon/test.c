#include <stdio.h>
#include <time.h>
#include <unistd.h>

void init_daemon(); 

int main()
{
    FILE *fp;
    time_t t;
    init_daemon();

    while (1) {
        sleep(1);
        if ((fp = fopen("print_time", "a")) >= 0) {
            t = time(0);
            fprintf(fp, "The time right now is : %s", asctime(localtime(&t)));
            fclose(fp);
        }
    }

    return 0;
}
