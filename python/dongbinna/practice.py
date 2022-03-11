# 정렬이란 데이터를 특정한 기준에 나열하는 것

# 선택 정렬 (selection sort)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j

    array[i], array[min_idx] = array[min_idx], array[i]

print(array)
