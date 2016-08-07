#ifndef _SEMAP_H_
#define _SEMAP_H_
union semun {
	int val;
	struct semid_ds *buf;
	unsigned short *array;
};
#endif
