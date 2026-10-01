import math
def solution(n):
    x = math.isqrt(n)
    if n == x ** 2:
        return (x+1) ** 2
    else:
        return -1
