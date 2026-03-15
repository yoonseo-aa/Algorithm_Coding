N = int(input())
arr = list(map(int, input().split()))
pc = [0] * 101
cnt = 0
for a in arr:
    if pc[a] == 0:
        pc[a] = 1
    else:
        cnt += 1

print(cnt)