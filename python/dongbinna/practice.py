#피보나치 수열

# 1 1 2 3 5 8 13 21 ...

# 일반적인 피보나치 수열, 계산한 결과도 다시 계산하여 사용

#fibo(40) 시 소요시간 : 24s

def fibo(x):

    if x<=2:
        return 1
    
    return fibo(x-1)+fibo(x-2)

print(fibo(40))
 