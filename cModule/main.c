#include "car.h"
// new
#include <dlfcn.h>
#include <stdlib.h>

// extern struct Car van;
//extern struct Car truck;

struct Car *car;
/*
void register_module(struct Car *module)
{
    car = module;
}*/

struct Car *register_module(char *module_name, void **p_handle)
{
    struct Car *(*get_module)();

    *p_handle = dlopen(module_name, RTLD_LAZY);
    if (!(*p_handle)) {
        return NULL;
    }

    get_module = dlsym(*p_handle, "get_module");
    if (dlerror() != NULL) {
        dlclose((*p_handle));
        return NULL;
    }

    return get_module();
}

void unregister_module(void *handle) 
{
    dlclose(handle);
}

int main(int argc, char *argv[])
{
    //register_module(&truck);
    //register_module(&van);
    
    struct Car *car;
    void *handle = NULL;
    if ((car = register_module("./van.so", &handle)) == NULL) 
        return -1;

    car->run();
    car->stop();

    unregister_module(handle);

    return 0;
}
