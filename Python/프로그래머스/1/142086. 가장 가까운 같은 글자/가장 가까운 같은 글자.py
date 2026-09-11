def solution(s):
    answer = []
    for i in range(len(s)):
        idx = s[:i].rfind(s[i])
        if idx < 0:
            answer.append(-1)
        else:
            answer.append(i-idx)
    return answer