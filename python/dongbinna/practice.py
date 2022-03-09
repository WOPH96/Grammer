#유클리드 호제법을 사용한 GCD 구하기


# A>B일 때 A를 B로 나눈 나머지 = R
# A와 B의 최대공약수 = B와 R의 최대공약수

#재귀함수는 점화식에서도 유용하게 사용 가능

def GCD(a,b):
    
    if(a%b==0):
        return b
    else:
        return GCD(b,a%b)


print(GCD(192,162))