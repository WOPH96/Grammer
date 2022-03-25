#include <algorithm>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    std::vector<int> vec;
    cout << "hello" << endl;
    string a;
    cin >> a;
    cout << stoi(a, nullptr, 16) << endl;
}