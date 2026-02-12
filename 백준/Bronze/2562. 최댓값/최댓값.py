arr = []
for i in range(9):
    num = int(input())
    arr.append(num)

max_v = float('-inf')
max_idx = 0
for j in range(9):
    if max_v < arr[j]:
        max_v = arr[j]
        max_idx = j+1

print(max_v)
print(max_idx)