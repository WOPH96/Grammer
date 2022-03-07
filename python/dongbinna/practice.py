# 람다 표현식 예시

array = [('홍길동', 50), ('이순신', 80), ('양원필', 75)]

print(array)

print(sorted(array, key=lambda x: x[1]))
print(array)

array.sort(reverse=True, key=lambda x: x[1])
print(array)

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

result = map(sum, lst1, lst2)  # 각각의 원소에 함수를 적용하고싶을 떄 map 사용

print(list(result))
