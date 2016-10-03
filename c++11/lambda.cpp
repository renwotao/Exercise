#include <iostream>
using namespace std;

/*
    lamda表达式
    [=] () mutable throw () ->int { expr };
    []: 捕获字段，默认捕获字段为[]时，lambda表达式是不能范文任何外部变量的，
        即表达式的函数体内无法访问当前作用域下的变量
    mutalbe: 捕获的变量可否修改
    throw(): 异常设定
    ():函数的形参列表
    ->int: lambda表达式函数的返回值类型
    {}: 大括号内为 lambda 表达式的函数体

 */

int main()
{
    auto add = [](int a, int b)->int{ return a + b; };
    int ret = add(1,2);
    cout << "ret: " << ret << endl;


    int x = 4;
    int y = 5;

    // 按值访问x,y
    auto add1 = [=] { return x + y; };
    auto add2 = [x,y] { return x + y; };
    cout <<"ret1: " << add1() <<" ret2: " << add2() << endl;
    // 按引用访问x,y
    cout << "x: " << x << " y: " << y << endl;
    auto add3 = [&] { x++; y++; return x+y; };
    auto add4 = [&x, &y] { x++; y++; return x+y; };
    cout << "ret3: " << add3() << endl;
    cout << "x: " << x << " y: " << y << endl;
    cout << "ret4: " << add4() << endl;
    return 0;
}
