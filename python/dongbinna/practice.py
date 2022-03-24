#금광 캐기

def maxmining(gold):

    

    return g

T = int(input())


tmp = []
gold= []
for _ in range(T):
    n,m = map(int,input().split())
    
    tmp.extend(list(map(int,input().split())))
    k=0
    for i in range(n):
        lst =[]
        for j in range(m):
            lst.append(tmp[k])
            k+=1
        gold.append(lst)  #다른 방법이 있을 듯 한데..

    print(maxmining(gold))    
    


print(gold)
        
