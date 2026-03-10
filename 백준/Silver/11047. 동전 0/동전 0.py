N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
cnt = 0
for i in range(N):
    cnt += K // arr[i]
    K = K % arr[i]

print(cnt)