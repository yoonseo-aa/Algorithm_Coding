n = int(input())
meetings = []

for _ in range(n):
    # 시작시간, 종료시간
    start, end = map(int, input().split())
    meetings.append((start, end))

# 전략 : 회의가 끝나는 시간을 기준으로 정렬(람다함수)
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = meetings[0][1] # 가장 빨리끝나는 회의의 끝나는 시간

for i in range(1, n):
    # 뒤 회의의 시작시간이 앞 회의의 끝나는 시간보다 크거나 같아야한다.
    if meetings[i][0] >= end_time:
        cnt += 1
        end_time = meetings[i][1] # 끝나는 시간 갱신

print(cnt)