#include <iostream>
#include <set> // TREE 구조
using namespace std;

template <typename T>
void print_set(set<T> &s)
{
    for (const T &itr : s)
    {
        cout << itr << " ";
    }
    cout << endl;
}

int main()
{

    set<int> s; // TREE 구조 , 중복 원소 없음

    s.insert(10);
    s.insert(50);
    s.insert(20);
    s.insert(40);
    s.insert(30); // 어디에 넣는지는 명시안함 => 순서정렬돼서 나옴

    print_set(s);

    auto itr = s.find(20); // set<>::iterator 반환,

    cout << "20 is in set?" << endl;
    if (itr != s.end())
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }

    itr = s.find(25);
    cout << "25 is in set?" << endl;
    if (itr != s.end())
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}
