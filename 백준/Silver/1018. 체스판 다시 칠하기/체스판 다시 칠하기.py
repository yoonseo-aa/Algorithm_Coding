N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

min_v = float('inf')

for i in range(N-7):
    for j in range(M-7):

        cnt1 = 0
        cnt2 = 0

        for y in range(i, i+8):
            for x in range(j, j+8):
                if (y + x) % 2 == 0:
                    if board[y][x] != 'W':
                        cnt1 += 1
                    if board[y][x] != 'B':
                        cnt2 += 1
                else:
                    if board[y][x] != 'B':
                        cnt1 += 1
                    if board[y][x] != 'W':
                        cnt2 += 1

        min_v = min(min_v, cnt1, cnt2)

print(min_v)
