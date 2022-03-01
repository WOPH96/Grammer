#include <iostream>

class Array
{
private:
    const int dim; // 몇 차원 배열인지
    int *size;     // size[0] * size[1] * ... * size[dim - 1] 짜리 배열이다.

    typedef struct
    {
        int level;
        // 맨 마지막 레벨(dim - 1 레벨) 은 데이터 배열을 가리키고, 그 위 상위
        // 레벨에서는 다음 Address 배열을 가리킨다.
        void *next;
    } Address;

    Address *top;

public:
    Array(int dim, int *array_size) : dim(dim)
    {
        size = new int[dim];
        for (int i = 0; i < dim; i++)
            size[i] = array_size[i];
    }
};

int main()
{

    return 0;
}