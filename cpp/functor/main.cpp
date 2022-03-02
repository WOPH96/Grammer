#include <iostream>

using std::cout;
using std::endl;
using std::string;

template <typename T>
struct Compare
{
    bool operator()(const T &a, const T &b) const { return a < b; }
};

template <typename T, typename Comp = Compare<T> >
T min(T &a, T &b)
{
    Comp comp;
    if (comp(a, b))
        return a;
    else
        return b;
    //   return a < b;
}

int main()
{
    int x = 3;
    int y = 5;
    cout << min(y, x) << endl;
}