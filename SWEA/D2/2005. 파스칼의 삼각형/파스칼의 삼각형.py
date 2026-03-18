"""
파스칼의 삼각형
1. 첫째줄은 항상 1이다.
2. 두 번째 줄은 자신의 왼쪽과 오른쪽 위의 합이다. (값이 없으면 0으로 처리)

- 이전의 값들을 dp에 저장
- dp에서 현재 인덱스 i와 i-1에 저장된 값의 합을 현재 값으로 함
- index 범위를 넘어가면 0으로 처리
"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    dp = [[] for _ in range(N+1)]

    for n in range(1, N+1):
        for i in range(n):
            if i == 0:
                dp[n].append(1)
            else:
                length = len(dp[n-1])

                if i >= length:
                    dp[n].append(dp[n-1][i-1])
                    continue

                dp[n].append(dp[n-1][i-1]+dp[n-1][i])
    print(f'#{tc}')
    for lst in dp[1:]:
        print(*lst)
