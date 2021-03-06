#include <iostream>
#include <string.h>

class MyString
{
private:
    char *string_content; // length가 있기에, NULL은 제외
    int string_length;    // 실제 문자 크기
    int memory_capacity;

public:
    MyString(char c);
    MyString(const char *str);
    MyString(const MyString &cpstr);
    ~MyString();

    int length() const;
    int capacity() const;
    void reserve(int size);
    void print() const;

    // MyString을 반환하여 다시 클래스 내 객체가 된다..!!
    // ==> 클래스 함수들을 사용 가능하게 한다
    // a.insert(b).length() 등...
    MyString &assign(const MyString &str);
    MyString &assign(const char *str);
    char at(int i) const;

    MyString &insert(int loc, const MyString &str);
    MyString &insert(int loc, const char *str);
    MyString &insert(int loc, char c);

    MyString &erase(int loc, int num);

    int find(int find_from, const MyString &str) const;
    int find(int find_from, const char *str) const;
    int find(int find_from, char c) const;
    int compare(const MyString &str) const;

    bool operator==(MyString &str);
};

MyString::MyString(char c)
{
    string_content = new char[1];
    string_content[0] = c;
    string_length = 1;
    memory_capacity = 1;
}
MyString::MyString(const char *str)
{
    string_length = strlen(str);
    // int len = 0; ==> strlen
    // while (*str)
    // {
    //     len++;
    //     str++;
    // }
    // string_length = len;
    string_content = new char[string_length];

    strcpy(string_content, str);

    // for (int i = 0; i < string_length; i++) ===> strcpy
    // {
    //     *(string_content + i) = str[i];
    // }
    memory_capacity = string_length;
    // std::cout << string_content << std::endl;
}
MyString::MyString(const MyString &cpstr) : string_length(cpstr.string_length)
{
    this->string_content = new char[this->string_length];

    strcpy(string_content, cpstr.string_content);
    // for (int i = 0; i < this->string_length; i++)
    // {
    //     *(this->string_content + i) = cpstr.string_content[i];
    // }

    memory_capacity = string_length;
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

int MyString::capacity() const
{
    return memory_capacity;
}
void MyString::reserve(int size)
{
    if (size > memory_capacity)
    {
        if (size < memory_capacity * 2)
            size = memory_capacity * 2;
        char *prev_string_content = string_content;

        string_content = new char[size];
        memory_capacity = size;

        for (int i = 0; i != string_length; i++)
            string_content[i] = prev_string_content[i];

        delete[] prev_string_content;
    }
}

void MyString::print() const
{
    for (int i = 0; i < string_length; i++)
        std::cout << string_content[i];

    std::cout << "\n";
}

MyString &MyString::assign(const MyString &str)
{
    if (str.string_length > memory_capacity) // 재할당 해주기
    {

        delete[] string_content; // assign 할꺼니까, 기존 값은 필요없음

        this->string_length = str.string_length; // private 함수는 같은 class만 접근가능
        this->memory_capacity = this->string_length;

        string_content = new char[this->memory_capacity];
    }

    strcpy(string_content, str.string_content);

    string_length = str.string_length;

    // for (int i = 0; i < str.string_length; i++)
    // {
    //     string_content[i] = str.string_content[i];
    // }

    return *this;
}
MyString &MyString::assign(const char *str)
{
    MyString temp(str);
    return this->assign(temp);
}
char MyString::at(int i) const
{

    if (i < 0 && i >= length())
        return (char)NULL;

    return string_content[i];
}

MyString &MyString::insert(int loc, const MyString &str)
{

    /* 굳이 나누지 않고 다시 짜보기!! */
    //선제조건
    //  a b c  ==> 기존 string이라 가정하면
    // 0 1 2 3  ==> 자리에만 놓일 수 있음.
    // 0<=loc<=length

    //공간
    // q w e r ==> 들어오는 데이터라면 총 공간 7개 필요
    // this->length + str.length > this->capacity == 재할당 필요

    //삽입
    // 0위치 삽입시
    // str_content 위치 저장 => char *temp = this->content
    // this->content = str.content
    // this->content[str.length+ i] = temp[i] for i in range(this->length)

    // this->length 위치 삽입시

    // this->content[this->length+ i] = str_content[i] for i in range(str.length)

    // 사이 삽입시 (e.g 1위치)
    // char* front = [:1) , char* back =[1:] X
    // char* back = [1:]만 설정 후 MyString temp(back); => 복사도 됨
    // this->content[1+i] = str.content[i] for i in range(str_length)
    // this->content[1+str_length] = temp.content[i] for i in range(temp_length)

    //완성
    //  a q w e r b c
    // 0 1 2 3 4 5 6 7

    //선제 조건
    if (loc < 0)
        loc = 0;
    else if (loc > this->string_length)
        loc = this->string_length;

    //공간 재설정
    string_length += str.string_length;
    reserve(string_length);
    // std::cout << this->memory_capacity;

    //삽입
    if (loc == 0)
    {
        MyString temp(this->string_content);

        strcpy(this->string_content, str.string_content);
        for (int i = 0; i < this->string_length; i++)
            this->string_content[str.string_length + i] = temp.string_content[i];
    }

    else if (loc == this->string_length)
    {
        for (int i = 0; i < str.string_length; i++)
            this->string_content[this->string_length + i] = str.string_content[i];
    }

    else
    {
        MyString back(&(this->string_content[loc]));
        for (int i = 0; i < str.string_length; i++)
            this->string_content[loc + i] = str.string_content[i];
        for (int i = 0; i < back.string_length; i++)
            this->string_content[loc + str.string_length + i] = back.string_content[i];
    }

    return *this;
}
MyString &MyString::insert(int loc, const char *str)
{
    MyString temp(str);
    return this->insert(loc, temp);
}
MyString &MyString::insert(int loc, char c)
{
    MyString temp(c);
    return this->insert(loc, temp);
}

MyString &MyString::erase(int loc, int num)
{
    //  a b c d e
    // 0 1 2 3 4 5
    // 0,3 ==>de = 0,1 = 3,4
    // 1,1 ==>acde = 1,2,3 = 2,3,4
    // 3,1 ==>abce = 3 = 4

    if (loc < 0 || loc >= string_length)
    {
        return *this;
    }

    else if (loc + num > string_length)
    {
        return *this;
    }

    for (int idx = loc; idx < loc + num; idx++)
    {
        std::cout << idx << std::endl;
        string_content[idx] = string_content[idx + num];
    }
    string_length -= num;

    return *this;
}

int MyString::compare(const MyString &str) const
{
    // (*this) - (str) 을 수행해서 그 1, 0, -1 로 그 결과를 리턴한다
    // 1 은 (*this) 가 사전식으로 더 뒤에 온다는 의미. 0 은 두 문자열
    // 이 같다는 의미, -1 은 (*this) 가 사전식으로 더 앞에 온다는 의미이다.
    for (int i = 0; i < std::min(string_length, str.string_length); i++)
    {
        if (string_content[i] > str.string_content[i])
            return 1;

        else if (string_content[i] < str.string_content[i])
            return -1;
    }

    // 여기 까지 했는데 끝나지 않았다면 앞 부분 까지 모두 똑같은 것이 된다.
    // 만일 문자열 길이가 같다면 두 문자열은 아예 같은 문자열이 된다.

    if (string_length == str.string_length)
        return 0;

    // 참고로 abc 와 abcd 의 크기 비교는 abcd 가 더 뒤에 오게 된다.
    else if (string_length > str.string_length)
        return 1;

    return -1;
}

bool MyString::operator==(MyString &str)
{
    return !this->compare(str);
}

int main()
{
    /*
        // MyString origin("abc");
        // MyString inserted("qwer");
        // origin.insert(3, inserted);
        // origin.print();

        // MyString str1("very long string");
        // MyString str2("<some string inserted between>");
        // str1.reserve(30);

        // std::cout << "Capacity : " << str1.capacity() << std::endl;
        // std::cout << "String length : " << str1.length() << std::endl;
        // str1.print();

        // str1.insert(5, str2);
        // str1.print();
        // std::cout << "Capacity : " << str1.capacity() << std::endl;
        // std::cout << "String length : " << str1.length() << std::endl;

        // MyString origin("qwertyuiop");
        // // MyString inserted("qwer");
        // // origin.insert(3, inserted);
        // // origin.print();
        // // std::cout << "String length : " << origin.length() << std::endl;
        // // origin.erase(4, 30);
        // // origin.print();
        // // std::cout << "String length : " << origin.length() << std::endl;

        // MyString sub("abcde");

        // std::cout << origin.compare(sub) << std::endl;
        */

    // 연산자 오버로딩
    MyString A("BBQ");
    MyString B("BBQ");

    std::cout << (A == B) << std::endl;
    return 0;
}