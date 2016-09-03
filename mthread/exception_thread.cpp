#include <thread>
#include <iostream>

class thread_guard
{
    std::thread& t;
public:
    explicit thread_guard(std::thread& t_): t(t_) {}
    ~thread_guard() {
        if (t.joinable()) {
            t.join();
        }
    }

    // 拷贝构造和拷贝赋值运算符被标记为 delete ,以确保编译器不会自动生成
    thread_guard(thread_guard const&)=delete;
    thread_guard& operator=(thread_guard const&)=delete;
};

struct func
{
    int &i;
    func(int& i_):i(i_) {}
    void operator()() {
        for (unsigned j = 0; j < 1000000; ++j) {
            std::cout << "do something" << std::endl;
        }
    }
};

int main()
{
    int some_local_state = 0;
    func my_func(some_local_state);
    std::thread t(my_func);
    thread_guard g(t);

}
