#include <stdlib.h>
#include <stdio.h>
#include "car.h"

static void run()
{
    printf("I am Truck, running...\n");
}

static void stop()
{
    printf("I am Truck, stopped...\n");
}

struct Car truck = {
.run = &run,
.stop = &stop,
};
