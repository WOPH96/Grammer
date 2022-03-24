#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

//정수 변환, stoi

int main()
{
    string str_dec = "2021,abc";
    string str_hex = "40c3";
    string str_bin = "-10101011";
    string str_auto = "0x14";

    string::size_type sz;

    int i_dec = stoi(str_dec, &sz);
    int i_hex = stoi(str_hex, nullptr, 16);
    int i_bin = stoi(str_bin, nullptr, 2);
    int i_auto = stoi(str_auto, nullptr, 0);

    cout << "i_dec : " << i_dec << str_dec.substr(sz) << endl;
    cout << "i_hex : " << i_hex << endl;
    cout << "i_bin : " << i_bin << endl;
    cout << "i_auto : " << i_auto << endl;
    return 0;
}