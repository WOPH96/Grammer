#include <iostream>
using std::string;

class Stack
{
    struct Node
    {
        Node *prev;
        string s;

        Node(Node *prev, string s) : prev(prev), s(s) {}
    };

    Node *current;
    Node start;

public:
    Stack();

    // 최상단에 새로운 원소를 추가한다.
    void push(string s);

    // 최상단의 원소를 제거하고 반환한다.
    string pop();

    // 최상단의 원소를 반환한다. (제거 안함)
    string peek();

    // 스택이 비어있는지의 유무를 반환한다.
    bool is_empty();

    ~Stack();
};

Stack::Stack() : start(NULL, "") { current = &start; };

void Stack::push(string s) // 새로운 노드 추가
{
    Node *n = new Node(current, s); //노드 생성
    current = n;                    // 현재노드 = n
}

// 최상단의 원소를 제거하고 반환한다.
string Stack::pop()
{
    if (current == &start) //만약 현재노드가 시작노드(가장 밑바닥이면)
        return "";         // 아무것도 반환하지 않는다

    string s = current->s;   // 현재 노드(맨위 노드)의 데이터를 담아둔다
    Node *prev = current;    // 현재 노드의 주소를 담아둔다
    current = current->prev; // 현재 노드 = 이전 노드를 가르킨다

    delete prev; // 현재 노드 삭제
    return s;    // 현재 노드 데이터 반환
}

// 최상단의 원소를 반환한다. (제거 안함)
string Stack::peek()
{
    return current->s; // 현재 노드의 데이터 반환
}

// 스택이 비어있는지의 유무를 반환한다.
bool Stack::is_empty()
{
    //현재 노드가 start를 가르키고, 데이터가 없으면 비어있음
    if (current == &start) //&& current->s == "")
        return true;
    else
        return false;
}
Stack::~Stack()
{
    while (current != &start)
    {
        Node *prev = current;
        current = current->prev;
        delete prev;
    }
}

int main()
{

    return 0;
}