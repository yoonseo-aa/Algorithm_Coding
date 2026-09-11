def solution(n):
    answer = 0
    res = ""
    while n > 0:
        res = str(n % 3) + res
        n //= 3
        
    return int(res[::-1],3)