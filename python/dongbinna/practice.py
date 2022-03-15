#개미전사

#창고를 하나건너 하나만 털 수 있음

#각 창고마다 최적해 구하기

# Ai = Max(Ai-1,Ai-2 + i)

food = [1,3,1,5]


DP=[0]*len(food)

DP[0] = food[0]
DP[1] = max(food[0],food[1])

for i in range(2,len(food)):
    DP[i] = max(DP[i-1],DP[i-2]+food[i])

print(DP[len(food)-1])