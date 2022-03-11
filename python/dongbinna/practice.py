# 정렬이란 데이터를 특정한 기준에 나열하는 것

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 퀵 정렬 (Quick sort)


def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot = left  # pivot 인덱스 저장
    end = right
    left += 1
    arr[pivot], arr[(right+left)//2] = arr[(right+left)//2], arr[pivot]
    while(left < right):
        while(left <= right and arr[left] < arr[pivot]):
            left += 1
        while(left <= right and arr[right] > arr[pivot]):
            right -= 1
        if(left < right):
            arr[left], arr[right] = arr[right], arr[left]
            print(arr)
    if arr[pivot] > arr[right]:
        arr[pivot], arr[right] = arr[right], arr[pivot]
    pivot, right = right, pivot
    print(arr, "pivot : ", pivot)

    quick_sort(arr, right, pivot-1)
    quick_sort(arr, pivot+1, end)


quick_sort(arr, 0, len(arr)-1)
print(arr)
