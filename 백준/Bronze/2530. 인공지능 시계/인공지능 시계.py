hour, minute, second = map(int, input().split())
time = int(input())

total = hour * 3600 + minute * 60 + second

total += time

total %= (24 * 3600)

h = total // 3600
m = (total % 3600) // 60
s = total % 60

print(h, m, s)
