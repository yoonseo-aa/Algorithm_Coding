N, K = map(int, input().split())
room_cnt = 0
male_cnt = [0] * 7
female_cnt = [0] * 7

for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        female_cnt[Y] += 1
    else:
        male_cnt[Y] += 1

min_v = 0

for i in range(1, 7):
    if 0 < female_cnt[i] < K:
        min_v += 1
    elif female_cnt[i] // K and female_cnt[i] % K == 0:
        min_v += female_cnt[i] // K
    elif female_cnt[i] % K > 0:
        min_v += (female_cnt[i] // K) + 1

for i in range(1, 7):
    if 0 < male_cnt[i] < K:
        min_v += 1
    elif male_cnt[i] // K and male_cnt[i] % K == 0:
        min_v += male_cnt[i] // K
    elif male_cnt[i] % K > 0:
        min_v += (male_cnt[i] // K) + 1

print(min_v)