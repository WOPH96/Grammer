#include <iostream>
#include <list>
using namespace std;

template <typename T>
void printlist(list<T> lst)
{
    for (const T &itr : lst)
        cout << itr << " ";
    cout << endl;
}

int main()
{
    list<int> lst;

    lst.push_back(10);
    lst.push_back(20);
    lst.push_back(30);

    cout << "처음 리스트 : ";
    printlist(lst);

    // for (int &itr : lst)
    // {
    //     cout << lst.begin() << " ";
    // }

    list<int>::iterator itr;

    for (itr = lst.begin(); itr != lst.end(); itr++)
    {
        if (*itr == 20)

            lst.insert(itr, 50);
    }

    printlist(lst);
    for (itr = lst.begin(); itr != lst.end(); itr++)
    {
        if (*itr == 50)
        {
            itr = lst.erase(itr);
        }
    }

    printlist(lst);

    return 0;
}
