from collections import deque

T = int(input())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for tc in range(1,T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1



    def bfs(y, x):
        visited = [[0] * M for _ in range(N)]
        visited[y][x] = 1
        q = deque()
        q.append((y,x))

        while q:
            y, x = q.popleft()
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
                if arr[ny][nx] == 1:
                    q.append((ny, nx))
                    arr[ny][nx] = 0

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)


