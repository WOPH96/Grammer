# 단순히 매 순간마다 큰 값을 고르는 것!

# 그리디 알고리즘 --> 문제 풀이를 위한 최소한의 아이디어를 떠올리는것이 중요

# N이 1이 될 때 까지

# 내 풀이


def solution(n, k):
    count = 0

    while(n != 1):
        if(n % k == 0):
            n //= k
            count += 1
        else:
            n -= 1
            count += 1

    return count


# 동빈나

# 최대한 많이 나누라

def bin_sol(n, k):
    result = 0
    while True:
        target = (n//k) * k  # 1을 빼는 과정을 몇번 하는가
        result += n-target
        n = target
        # N이 K보다 작을 때 탈출
        if n < k:
            break
        n //= k
        result += 1
    result += (n-1)
    return result


print(bin_sol(17, 4))
