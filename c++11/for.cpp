#include <iostream>
using namespace std;


int main()
{
    int numbers[] = {1, 2, 3, 4, 5};
    cout << "numbers:" << endl;
    for (auto number : numbers) {
        cout << number << endl;
    }
}
