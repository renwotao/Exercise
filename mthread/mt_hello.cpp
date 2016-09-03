#include <iostream>
#include <thread>
using namespace std;

class background_task
{
public:
    void operator()()const {
        cout << "do something" << endl;
    }
};

void hello()
{
    cout << "Hello world" << endl;
}

int main()
{
    // function
    thread t(hello);
    t.join();
    
    // callable 
    background_task f;
        // callable was copied to my_thread object
    thread my_thread(f);
    my_thread.join();
    
    // thread my_thread1(background_task()); // error, take background_task as function declaration
    thread my_thread2((background_task()));
    thread my_thread3{background_task()};
    //thread my_thread4 = {background_task()}; // error
    my_thread2.join();
    my_thread3.join();

    thread my_thread5([] { cout << "do something" << endl; });
    my_thread5.join();
}
