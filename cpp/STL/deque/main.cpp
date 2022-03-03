#include <iostream>
#include <deque>
using namespace std;

template <typename T>
void print_deque(deque<T> dq)
{
    for (const T &itr : dq)
        cout << itr << " ";
    cout << endl;
}

int main()
{
    deque<int> dq;
    dq.push_back(10);
    dq.push_back(20);
    dq.push_back(30);
    dq.push_front(40);
    dq.push_front(50);

    cout << "초기 dq :" << endl;
    print_deque(dq);

    cout << "맨앞 원소 제거 " << endl;
    dq.pop_front();
    print_deque(dq);

    return 0;
}
