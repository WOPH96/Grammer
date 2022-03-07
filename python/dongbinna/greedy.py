# 단순히 매 순간마다 큰 값을 고르는 것!

# 그리디 알고리즘 --> 문제 풀이를 위한 최소한의 아이디어를 떠올리는것이 중요

# 곱하기 혹은 더하기

# x or + 넣어서 가장 큰 수 만들기

# 0이 오면 덧셈 나머지는 곱셈 ==> 1이 와도 덧셈!

# 내 풀이

def solution(s):
    answer = int(s[0])
    flag = False

    if answer == 0 or answer == 1:
        answer += int(s[1])
        flag = True

    for n in s[1:]:
        if flag:
            flag = False
            continue
        if n == '0' or n == '1':
            answer += int(n)
        else:
            answer *= int(n)

    return answer


print(solution('02984'))
