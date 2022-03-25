#include <algorithm>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

// comp test

template <typename T1, typename T2>
void printv(vector<pair<T1, T2>> v)
{
    for (auto x : v)
    {
        cout << x.first << x.second << endl;
    }
    cout << endl;
};

int main()
{

    vector<pair<int, int>> a;

    a.push_back(pair<int, int>(1, 3));
    a.push_back(make_pair(4, 2));
    a.push_back(make_pair(6, 8));
    a.push_back(make_pair(3, 7));
    a.push_back(make_pair(1, 9));

    printv(a);
    sort(a.begin(), a.end());
    printv(a);
    sort(a.begin(), a.end(), [](pair<int, int> p1, pair<int, int> p2)
         {  
             if (p1.first != p2.first)
                return p1.first > p2.first;
             return p1.second < p2.second; });
    printv(a);
    // cout << vec[0].push_back(3) << endl;
}