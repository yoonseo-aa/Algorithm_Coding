n = int(input())
arr = list(map(int, input().split()))

add_cnt = 1
minus_cnt = 1
max_add_v = 1
max_minus_v = 1

for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]:
        add_cnt += 1
    else:
        add_cnt = 1

    if max_add_v < add_cnt:
        max_add_v = add_cnt

for i in range(len(arr) - 1):
    if arr[i] >= arr[i + 1]:
        minus_cnt += 1
    else:
        minus_cnt = 1

    if max_minus_v < minus_cnt:
        max_minus_v = minus_cnt

print(max(max_minus_v, max_add_v))
