#미로 탈출 
'''
(1,1)에서 시작하여, (N,M)위치로 탈출
0은 괴물이므로 피해서 가야함
한번에 한칸씩 이동 가능
'''

#BFS == 간선의 비용이 모두 같을 떄 최단거리를 탐색할 때 사용하는 

# 주변을 이동할 때마다 최단거리 증가

from collections import deque


n,m = map(int,input().split())

maze =[]

for i in range(n):
    maze.append(list(map(int,input())))

#방향 벡터 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]


#bfs
x,y = 0,0
q = deque()
q.append((x,y))

while q:
    x,y = q.popleft()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if tx<0 or tx >=n or ty<0 or ty>=m:
            continue

        if maze[tx][ty] == 0:
            continue

        if maze[tx][ty] == 1 : # 해당 노드 처음 방문 시
            maze[tx][ty] = maze[x][y]+1
            q.append((tx,ty))
print()
for i in maze:
    for j in i:
        print(j,end=" ")
    print()

print("최단거리 : ",maze[n-1][m-1])