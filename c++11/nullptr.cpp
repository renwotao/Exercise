#include <iostream>
using namespace std;

class Test
{
public:
    void TestWork(int index) {
        cout << "TestWork 1" << endl;
    }

    void TestWork(int *index) {
        cout << "TestWork 2" << endl;
    }
};


int main()
{
    Test test;
    //test.TestWork(NULL); // 编译不通过，函数调用二义性，编译器无法知道调用哪个TestWork
    test.TestWork(nullptr);

    int *p1 = nullptr;
    int *p2 = 0;
    int *p3 = NULL;
    cout << "test nullptr: " << (p1 == p2) << "\t" << (p1 == p3) << endl;
}
