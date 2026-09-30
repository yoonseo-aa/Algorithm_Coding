import math

def solution(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, math.isqrt(n)+1):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
    return is_prime.count(True)