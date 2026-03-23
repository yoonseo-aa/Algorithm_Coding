N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

max_v = 1

for y in range(N):
    for x in range(M):
        for k in range(1, min(N, M)):
            ny = y + k
            nx = x + k

            if ny >= N or nx >= M:
                break

            if arr[y][x] == arr[y][nx] == arr[ny][x] == arr[ny][nx]:
                max_v = max(max_v, (k+1)**2)

print(max_v)