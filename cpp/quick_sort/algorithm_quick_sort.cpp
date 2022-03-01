#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <algorithm>

using namespace std;
// Quick sort 구현
// 1 2 5 4 8 3 0 4 2 6 5 2 7 8
// pivot

#define n 14

void SWAP(int &a, int &b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
}

void printarr(int arr[], int size)
{

    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int sorting(int left, int right, int arr[])
{
    //첫번째 원소가 피벗
    int &pivot = left;

    // 첫번째 원소를 중간값과 교환 *** 중요 !!! ***
    SWAP(arr[pivot], arr[(int)((left + right) / 2)]);

    // cout << arr[pivot] << endl;

    int low = left + 1;
    int high = right;

    // cout << "first low : " << low << " high : " << high << endl;

    do
    {
        do
        {
            if (arr[low] > arr[pivot])
                break;
            low++;
        } while (low <= high);

        do
        {
            if (arr[high] < arr[pivot])
                break;
            high--;
        } while (low <= high);

        if (low < high)
        {
            // cout << "before_swap \t ";
            // printarr(arr);
            SWAP(arr[low], arr[high]);
            // cout << "after_swap \t ";
            // printarr(arr);
        }
    } while (low < high);
    // cout << "low : " << low << " high : " << high << endl;

    if (arr[high] < arr[pivot])
    {
        // cout << "before_swap \t ";
        // printarr(arr);
        SWAP(arr[high], arr[pivot]);
        // cout << "after_swap \t ";
        // printarr(arr);
        return high;
    }
    return pivot;
}

void quicksort(int left, int right, int arr[])
{

    if (left < right) // 0 or 1개가 아닐때까지
    {
        int p = sorting(left, right, arr); // 피벗 위치 반환

        // cout << "pivot " << p << endl;
        //  printarr(arr);

        quicksort(left, p - 1, arr); // 0 3
        quicksort(p + 1, right, arr);
    }
}
bool cmp(const int a, const int b)
{
    return b < a;
}

int main()
{
    // int arr[] = {1, 2, 5, 4, 8, 3, 7, 4, 2, 6, 5, 2, 7, 8};
    // // printarr(arr);
    // int size = sizeof(arr) / sizeof(arr[0]);

    int arr[100000];

    srand((int)time(NULL));
    for (int i = 0; i < 100000; i++)
    {
        arr[i] = rand() % 3000000;
    }
    int size = 100000;

    clock_t start, finish;
    double duration;

    start = clock();
    quicksort(0, size - 1, arr);
    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    // printarr(arr, size);
    cout << "quick sort : " << duration << "s" << endl;

    start = clock();
    sort(arr, arr + size, cmp);
    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    cout << "algorithm sort : " << duration << "s" << endl;
    // printarr(arr, size);

    start = clock();
    quicksort(0, size - 1, arr);
    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    // printarr(arr, size);
    cout << "quick sort : " << duration << "s" << endl;

    return 0;
}