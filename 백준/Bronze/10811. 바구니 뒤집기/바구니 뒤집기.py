N, M = map(int, input().split())

basket = [0] + [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i:j+1] = reversed(basket[i:j+1])

print(*basket[1:])
