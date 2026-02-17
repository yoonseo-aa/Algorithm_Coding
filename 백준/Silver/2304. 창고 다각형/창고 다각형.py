import sys
input = sys.stdin.readline

N = int(input())
pillars = []

for _ in range(N):
    L, H = map(int, input().split())
    pillars.append((L, H))

pillars.sort()

max_height = 0
max_index = 0

for i in range(N):
    if pillars[i][1] > max_height:
        max_height = pillars[i][1]
        max_index = i

area = 0

left_max = pillars[0][1]
for i in range(max_index):
    left_max = max(left_max, pillars[i][1])
    width = pillars[i+1][0] - pillars[i][0]
    area += left_max * width

right_max = pillars[-1][1]
for i in range(N-1, max_index, -1):
    right_max = max(right_max, pillars[i][1])
    width = pillars[i][0] - pillars[i-1][0]
    area += right_max * width

area += max_height 

print(area)