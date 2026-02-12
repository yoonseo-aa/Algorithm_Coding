arr = []
for _ in range(10):
    num = int(input())
    arr.append(num)

cnt = {}
for i in range(10):
    remain = arr[i] % 42
    if remain not in cnt:
        cnt[remain] = 0
    cnt[remain] += 1

print(len(cnt))