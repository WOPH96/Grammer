#include <iostream>
#include <string.h>

class MyString
{
private:
    char *string_content; // length가 있기에, NULL은 제외
    int string_length;    // 실제 문자 크기

public:
    MyString(char c);
    MyString(const char *str);
    MyString(const MyString &cpstr);
    ~MyString();

    int length() const;
    void show_str() const;
};

MyString::MyString(char c)
{
    string_content = new char[1];
    string_content[0] = c;
    string_length = 1;
}
MyString::MyString(const char *str)
{
    string_length = strlen(str);
    string_content = new char[string_length];
    for (int i = 0; i < string_length; i++)
    {
        *(string_content + i) = str[i];
    }
    // std::cout << string_content << std::endl;
}
MyString::MyString(const MyString &cpstr) : string_length(cpstr.string_length)
{
    this->string_content = new char[this->string_length];
    for (int i = 0; i < this->string_length; i++)
    {
        *(this->string_content + i) = cpstr.string_content[i];
    }
    // std::cout << this->string_content << std::endl;
}
MyString::~MyString()
{
    delete[] string_content;
}

int MyString::length() const
{
    return string_length;
}

void MyString::show_str() const
{
    std::cout << string_content << std::endl;
}

int main()
{
    MyString a("abc");
    MyString b(a);
    MyString c = a;
    b.length();
    b.show_str();
    return 0;
}