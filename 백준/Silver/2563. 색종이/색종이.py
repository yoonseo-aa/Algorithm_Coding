N = int(input())
board = [ [0] * 101 for _ in range(101)]

for _ in range(N):
    n1, n2 = map(int, input().split())
    for y in range(n1, n1+10):
        for x in range(n2, n2+10):
            board[y][x] = 1

result = 0

for b in board:
    n = b.count(1)
    result += n

print(result)