N = int(input())
score = list(map(int, input().split()))
max_v = max(score)
sum_v = 0
for i in range(N):
    sum_v += score[i]/max_v*100
print(sum_v/N)