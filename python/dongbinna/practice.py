#효율적인 화폐 구성

#많은 걸 최대한 많이 사용..하면 안되나?

#16원 => 3*4 + 2*2 = 6개

#   16원
#  각 금액별로 최소화폐를 적는다
# d[i] = i원을 만들기 위한 최소화폐
# d[1] = 10000
# d[2] = 1
# d[3] = 1
# d[4] = d[2]+d[2] =2
# d[5] = d[3]+d[2] =2
# d[6] = min(d[4]+d[2],d[3]+d[3])
# d[7] = min(d[3]+d[7-3],d[2]+d[7-4])
# d[i] = min(d[M]+d[i-M],...,d[m]+d[i-m])
# --> min보다는 M으로 했을때 되길 바라보자


n,m = map(int,input().split())

coins =[]
for _ in range(n):
    coins.append(int(input()))

d = [10000]* 101

coins.sort(reverse=True)

for coin in coins:
    d[coin] = 1


for i in range(max(coins)+1,m+1):
    for coin in coins: # 큰값부터 체크
        d[i] = d[coin]+d[i-coin] # 
        if d[i] < 10000: break # 제대로 개수 취한거

if d[m]>=10000:
    d[m] = -1

print("최소화폐개수 = ",d[m])

