def solution(n):
    m = n // 2
    if n % 2 == 0:
        return "수박" * m
    else:
        return "수박" * m + "수"
