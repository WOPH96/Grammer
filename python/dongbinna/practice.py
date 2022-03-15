#피보나치 수열

# 1 1 2 3 5 8 13 21 ...

# 다이나믹 프로그래밍 사용
# DP table을 이용한다

# 탑다운


def fibo(x):

    if x<=2:
        DP[x]=1
        return 1
    
    if DP[x] != 0 :
        return DP[x]

    DP[x] = fibo(x-1)+fibo(x-2)

    return DP[x]

n = int(input())

DP = [0]*(n+1)

print(fibo(n))
 