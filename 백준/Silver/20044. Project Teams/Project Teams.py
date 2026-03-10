n = int(input()) # 팀 수
arr = list(map(int, input().split()))
arr.sort()
team = []
for i in range(n):
    a = arr.pop(0)
    b = arr.pop()
    team.append((a,b))

min_v = float('inf')
for t in team:
    res = t[0] + t[1]
    min_v = min(min_v, res)

print(min_v)