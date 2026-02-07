sum = 0
n = list(map(int,input().split()))
for i in range(5):
    sum += n[i]**2

print(sum%10)