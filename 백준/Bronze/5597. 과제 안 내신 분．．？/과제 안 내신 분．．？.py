arr = [0] * 31
for i in range(1,29):
    num = int(input())
    arr[num] = 1

for j in range(1,31):
    if arr[j] == 0:
        print(j)

