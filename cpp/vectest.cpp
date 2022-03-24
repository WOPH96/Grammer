#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

//

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

    vector<int> v(8);

    printvec(v);

    fill(v.begin(), v.begin() + 4, 5);
    printvec(v);

    fill(v.begin() + 3, v.end() - 2, 8);
    printvec(v);

    fill_n(v.begin(), distance(v.begin(), v.end()), 15);
    printvec(v);

    vector<int> myvec = {1, 3, 2};
    printvec(myvec);

    vector<int> myvec2(10, 3);
    printvec(myvec2);

    return 0;
}