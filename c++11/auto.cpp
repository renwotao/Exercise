#include <iostream>
using namespace std;

/*
    auto 在 c++14 中可以作为函数的返回值
    auto 作为函数返回值时，只能用于定义函数，不能用于声明函数
    若函数实现也写在头文件中，则可以编译通过
 */

auto AddTest(int a, int b) 
{
    return a+b;
}

int main()
{
    auto index = 10;
    auto str = "abc";
    auto ret = AddTest(1, 2);
    cout << "index: " << index << endl;
    cout << "str: " << str << endl;
    cout << "res: " << ret << endl;
}
