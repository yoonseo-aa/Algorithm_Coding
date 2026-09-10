def solution(x):
    sum_x = sum(list(map(int, str(x))))
    if x % sum_x == 0:
        return True
    else:
        return False
