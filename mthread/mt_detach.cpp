#include <unistd.h>
#include <thread>
#include <iostream>
#include <cassert>
using namespace std;


void print_hello()
{
	do {
		sleep(1);
		cout << "hello" << endl;
	} while (1);
}

int main()
{
	thread t(print_hello);
	t.detach();
	assert(!t.joinable());
	sleep(5);
}
