import math

def solution(progresses, speeds):
    answer = []
    days = []

    # 각 기능이 완료되는 날짜
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)

    standard = days[0]
    count = 1

    for i in range(1, len(days)):
        if days[i] <= standard:
            count += 1
        else:
            answer.append(count)
            standard = days[i]
            count = 1

    answer.append(count)

    return answer