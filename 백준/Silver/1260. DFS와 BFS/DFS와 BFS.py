from collections import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

def bfs(s, graph, visited):
    que = deque([s])
    visited[s] = True

    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

def dfs(v, graph, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph, visited)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)
visited2 = [False] * (N+1)

dfs(V, graph, visited2)
print()
bfs(V, graph, visited)