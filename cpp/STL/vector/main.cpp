#include <iostream>
#include <vector>
using namespace std;

template <typename T>
void printvec(vector<T> vec)
{
    for (typename vector<T>::iterator itr = vec.begin(); itr != vec.end(); ++itr)
        cout << *itr << " ";
    cout << endl;
}

template <typename T>
void printvec_const(vector<T> vec)
{
    vector<int>::const_iterator citr = vec.begin();
    for (; citr != vec.end(); citr++)

        cout << *citr << " ";

    cout << endl;
}

template <typename T>
void rprintvec(vector<T> vec)
{
    for (typename vector<T>::reverse_iterator itr = vec.rbegin(); itr != vec.rend(); ++itr)
        cout << *itr << " ";
    cout << endl;
}

template <typename T>
void print_range(vector<T> vec)
{
    for (const T &elem : vec)
    {
        cout << elem << " ";
    }
    cout << endl;
}

int main()
{

    vector<int> vec;

    vec.push_back(10);
    vec.push_back(20);
    vec.push_back(30);

    // for (vector<int>::iterator itr = vec.begin(); itr != vec.end(); ++itr)
    // {
    //     cout << *itr << endl;
    // }
    printvec(vec);
    vec.insert(vec.end(), 40);
    printvec(vec);
    vec.insert(vec.begin() + 1, 50);
    printvec(vec);
    printvec_const(vec);
    vec.erase(vec.begin() + 3);
    rprintvec(vec);

    print_range(vec);

    return 0;
}