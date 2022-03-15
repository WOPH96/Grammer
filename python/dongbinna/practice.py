#피보나치 수열

# 1 1 2 3 5 8 13 21 ...

# 다이나믹 프로그래밍 사용
# DP table을 이용한다

# 바텀업


def fibo(x):

    DP = [0]*(n+1)

    DP[1] = 1
    DP[2] = 1

    for i in range(3,x+1):
        DP[i] = DP[i-1] + DP[i-2]

    return DP[x]
n = int(input())


print(fibo(n))
 