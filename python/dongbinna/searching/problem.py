#음료수 얼려 먹기 

#connected 어쩌고

# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1<=N, M<=1000)
# 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0 그렇지 않은 부분은 1

# 0번과 연결된 모든 노드를 방문 => 방문 처리가 이뤄지는데에서만 카운트하기

#동빈나 풀이 ㅜ

def dfs(x,y):
    if x <0 or x>=n or y<0  or y>=n :
        return False
    if graph[x][y] == 0 : # 연결된 지점들에 전부 방문처리
        graph[x][y] =1 

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)

        return True
    return False

result =0 

n, m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

for i in range(n):
    for j in range(m):
        if(dfs(i,j)) == True:
            result+=1


print(result)