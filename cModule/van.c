#include <stdlib.h>
#include <stdio.h>
#include "car.h"

static void run()
{
    printf("I am Van, running...\n");
}

static void stop()
{
    printf("I am Van, stoppted...\n");
}

/*
struct Car van = {
    .run = &run,
    .stop = &stop,
};*/

struct Car module = {
    .run = &run,
    .stop = &stop,
};

struct Car *get_module()
{
    return &module;
}
