def solution(n):
    answer = 0
    digit = str(n)
    for i in digit:
        answer += int(i)

    return answer