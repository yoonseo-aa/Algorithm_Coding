def solution(n):
    res = list(str(n))
    res.sort(reverse=True)
    return int("".join(res))