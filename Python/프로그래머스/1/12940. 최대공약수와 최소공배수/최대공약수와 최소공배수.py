def solution(n, m):
    import math
    gcd_val = math.gcd(n, m)
    lcm_val = (n * m) /gcd_val
    return [gcd_val, lcm_val]