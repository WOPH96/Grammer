<<<<<<< HEAD
#금광 캐기

def maxmining(gold):

    

    return g

T = int(input())


tmp = []
gold= []
for _ in range(T):
    n,m = map(int,input().split())
    
    tmp.extend(list(map(int,input().split())))
    k=0
    for i in range(n):
        lst =[]
        for j in range(m):
            lst.append(tmp[k])
            k+=1
        gold.append(lst)  #다른 방법이 있을 듯 한데..

    print(maxmining(gold))    
    
=======
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
>>>>>>> 2e240878808e7e91ef91553eeab27445953b4766

    quick_sort(arr, right, pivot-1)
    quick_sort(arr, pivot+1, end)

<<<<<<< HEAD
print(gold)
        
=======

quick_sort(arr, 0, len(arr)-1)
print(arr)
>>>>>>> 2e240878808e7e91ef91553eeab27445953b4766
