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