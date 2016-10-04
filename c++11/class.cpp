#include <iostream>
#include <vector>
using namespace std;

class InitClass
{
public:
        void print_class() {
            cout << field1 << '\t' << field2 << '\t' << field3
                << '\t' << field4 << endl;
        }

private:
        int field1 = 1;
        int field2;
        double field3 = 1.0;
        double field4;
};

class InitClassMgr
{
public:
    vector<InitClass> init_objs { InitClass() };
};

int main()
{
    InitClass test_class;
    cout << "test class memeber initialization:\n";
    test_class.print_class();

    InitClassMgr mgr;
    cout << "test class member of class type initialization:\n";
    mgr.init_objs[0].print_class();

}
