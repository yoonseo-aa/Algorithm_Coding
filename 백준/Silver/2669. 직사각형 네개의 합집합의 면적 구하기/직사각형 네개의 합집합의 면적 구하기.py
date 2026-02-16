arr = [[0] * 100 for _ in range(100)]

for i in range(4):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = 1

num = 0
for a in arr:
    num += a.count(1)
    
print(num)
