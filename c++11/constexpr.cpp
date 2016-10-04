#include <iostream>
using namespace std;

int out_i = 0;

constexpr int sz() { return 42; }
constexpr int new_sz(int cnt) { return sz() * cnt; }
constexpr int size = sz();

int main()
{
    constexpr int mf = 20;
    constexpr int limit = mf + 1;

    // out_i 是全局变量，其地址不变
    constexpr int *p1 = &out_i;

    // constexpr 指针和 const 指针的含义完全相同
    constexpr int *p2 = nullptr;
    const int *p3 = nullptr;

    /*  constexpr 用于函数
        constexpr 函数是指能用于常量表达式的函数
        a. 返回类型时字面值类型
        b. 形参乐行时字面值类型
        c. 函数体中有且仅有一条 return 语句
    */
    constexpr int nsize = new_sz(mf);
    //constexpr int wrong_size = new_sz(out_i); // error: out_i is not a constexpr
    cout << "test constexpr: " << mf << '\t' << limit << '\t' << size << '\t' 
        << nsize << '\t' << p1 <<'\t' << p2 << '\t' << p3 << endl;

}
