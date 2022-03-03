#include <iostream>
#include <set> // TREE 구조
using namespace std;

template <typename T>
void print_set(set<T> &s)
{
    for (const T &itr : s)
    {
        cout << itr << " ";
    }
    cout << endl;
}

class Todo
{

    int priority;
    string job_descript;

public:
    Todo(int pr, string jd) : priority(pr), job_descript(jd) {}

    bool operator<(const Todo &t) const
    {
        if (this->priority == t.priority)
        {
            return this->job_descript > t.job_descript;
        }
        else
        {
            return this->priority < t.priority;
        }
    }

    friend ostream &operator<<(ostream &o, const Todo &t);
};

ostream &operator<<(ostream &o, const Todo &t)
{
    o << "[중요도 : " << t.priority << ", 해야하는 일 : " << t.job_descript << "]";

    return o;
}

int main()
{

    set<Todo> todos;

    todos.insert(Todo(1, "놀기"));
    todos.insert(Todo(2, "자기"));

    print_set(todos);

    return 0;
}
