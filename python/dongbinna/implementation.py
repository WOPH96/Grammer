# 구현 => 풀이를 떠올리는 것은 쉽지만 소스코르도 옮기기 어려운 문제

# 알고리즘은 간단한데 코드가 지나칠만큼 길어지는 문제
# 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
# 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 적절한 라이브러리를 찾아서 사용해야 하는 문제 eg) 순열, 조합

# 많은 코드를 작성하고 많은 라이브러리를 사용해본다면 쉽게 풀 수 있음.

# Simulation 유형 / 완전 탐색 / 구현 유형

# 나이트가 갈 수 있는 경우의 수 구하기

# 문자열 재정렬

# 숫자 = 0~9 한 글자를 의미
# 수 = 100 , 700 , 10000 등 정수 값을 의미

# S = str(input())

# lst = sorted(S)

# sum = 0
# # print(lst)
# # print(ord('0'))

# while ord(lst[0]) < 65:
#     sum += ord(lst[0])-ord('0')
#     lst.pop(0)
# S = "".join(lst)
# S += str(sum)


# print(S)

# 동빈나

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
