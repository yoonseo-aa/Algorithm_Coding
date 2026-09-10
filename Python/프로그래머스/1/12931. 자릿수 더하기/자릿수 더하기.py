def solution(n):
    answer = 0
    digit = list(map(int, str(n)))
    
    for i in range(len(digit)):
        answer += digit[i]
    return answer