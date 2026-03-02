from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
            if arr[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

bfs()
print(visited[N-1][M-1])