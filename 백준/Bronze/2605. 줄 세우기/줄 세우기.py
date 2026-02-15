N = int(input())
arr = list(map(int, input().split()))
line = []

for i in range(N):
    line.insert(len(line) - arr[i], i+1)

print(*line)
