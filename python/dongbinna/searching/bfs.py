# 너비 우선 탐색 BFS
# 가까운 노드부터 우선적으로 탐색
# 큐 자료구조 사용
'''
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리 
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모든 큐에 삽입하고 방문처리
3. 더이상 2번의 과정을 수행할 수 없을 때까지
'''
#특정 최단거리 문제로 사용된다.

from collections import deque

#내풀이

# def bfs(graph,init,visited):
#     queue = deque()
#     print(init, end= " ")
#     visited[init] = True
#     for i in graph[init]:
#         print(i, end =" ")
#         queue.append(i)
#         visited[i] = True
#     while queue :
#         visit = queue.popleft()
#         for i in graph[visit]:
#             if not visited[i]:
#                 print(i, end =" ")
#                 queue.append(i)
#                 visited[i] = True

#동빈나 
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



graph = [
    [], #0번노드
    [2,3,8], # 1번노드
    [1,7], # 2번노드
    [1,4,5], #3번노드
    [3,5], # 4번노드
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
bfs(graph,1,visited)