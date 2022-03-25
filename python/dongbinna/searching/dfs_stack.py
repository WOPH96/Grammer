
# DFS with Stack

def dfs(graph, start, visited):
    # 1번 노드 시작
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")
            for i in graph[node][::-1]:
                stack.append(i)
    print()


graph = [
    [],  # 0번노드
    [2, 3, 8],  # 1번노드
    [1, 7],  # 2번노드
    [1, 4, 5],  # 3번노드
    [3, 5],  # 4번노드
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
