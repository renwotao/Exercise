#include <iostream>
#include <array>
#include <forward_list>
using namespace std;


int main()
{
    array<int, 4> arr = {1, 2, 3, 4};
    cout << "array: ";
    for (auto item : arr) {
        cout << item << endl;
    }

    auto arr_size = sizeof(arr);
    cout << "array size: " << arr_size << endl;


    // 单向链表 forward_list
    forward_list<int> numbers={1, 2, 3, 4, 5, 4, 4};
    cout << "numbers: " << endl;
    for (auto number: numbers) {
        cout << number << endl;
    }

    numbers.remove(4);
    cout << "numbers after remove: " << endl;
    for (auto number: numbers) {
        cout << number << endl;
    }
    return 0;
}
