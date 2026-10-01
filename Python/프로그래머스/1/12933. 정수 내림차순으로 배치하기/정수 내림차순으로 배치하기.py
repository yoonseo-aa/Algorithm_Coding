def solution(n):
    res = list(map(int, str(n)))
    res.sort(reverse=True)
    answer = ""
    for r in res:
        answer += str(r)
    return int(answer)