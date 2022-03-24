#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// find 함수 테스트

template <typename T>
void printvec(vector<T> v)
{
    for (auto it = v.begin(); it != v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
}
int main()
{

    int arr[] = {235, 36, 2, 3, 23, 52, 51, 5, 1, 3, 6, 3};

    vector<int> v(arr, arr + sizeof(arr) / sizeof(arr[0]));
    printvec(v);

    sort(v.begin(), v.end());
    printvec(v);

    reverse(v.begin(), v.end());
    printvec(v);

    auto itr = find(v.begin(), v.end(), 36);

    if (itr != v.end()) // find!
        cout << distance(v.begin(), itr) << endl;
    else
        cout << "no found " << endl;

    auto itr2 = find_if(v.begin(), v.end(), [](int n)
                        { return n % 2 == 1; });
    while (itr2 != v.end())
    {
        cout << *itr2 << " is at v[" << distance(v.begin(), itr2) << "]" << endl;
        itr2 = find_if(itr2 + 1, v.end(), [](int n)
                       { return n % 2 == 1; });
    }

    return 0;
}