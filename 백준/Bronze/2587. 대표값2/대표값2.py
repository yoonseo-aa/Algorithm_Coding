arr = []
for _ in range(5):
    num = int(input())
    arr.append(num)

arr.sort()

avg_v = sum(arr) // 5
print(avg_v)
print(arr[2])