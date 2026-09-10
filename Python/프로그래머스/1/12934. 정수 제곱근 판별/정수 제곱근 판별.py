def solution(n):
    import math

    num = math.sqrt(n)
    if num.is_integer():
        return (num+1)**2
    else:
        return -1