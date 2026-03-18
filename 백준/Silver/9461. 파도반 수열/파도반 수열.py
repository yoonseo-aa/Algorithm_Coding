"""
dp에 지금까지 삼각형의 변의 길이 저장
현재 삼각형(i)의 변의 길이 k = dp[i-2] + dp[i-3]
만약 i-2나 i-3이 index 범위를 벗어나면 k = 1
"""
import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    dp = []
    for i in range(N):
        i1, i2 = i-2, i-3
        if i1 < 0 or i2 < 0:
            dp.append(1)
            continue

        dp.append(dp[i1]+dp[i2])

    print(f'{dp[-1]}')