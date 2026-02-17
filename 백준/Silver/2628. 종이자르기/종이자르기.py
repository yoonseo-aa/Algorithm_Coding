w, h = map(int, input().split())
N = int(input())
x_arr = [0, h]
y_arr = [0, w]
for _ in range(N):
    wh, line = map(int, input().split())
    if wh == 0:
        x_arr.append(line)
    else:
        y_arr.append(line)

x_arr.sort()
y_arr.sort()

max_x, max_y = 0, 0
for i in range(1, len(x_arr)):
    gap = x_arr[i] - x_arr[i-1]
    max_x = max(max_x, gap)

for i in range(1, len(y_arr)):
    gap = y_arr[i] - y_arr[i-1]
    max_y = max(max_y, gap)

print(max_x * max_y)