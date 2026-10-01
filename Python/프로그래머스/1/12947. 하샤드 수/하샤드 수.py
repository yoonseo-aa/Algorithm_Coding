def solution(x):
    s = sum(list(map(int,str(x))))
    if x % s == 0:
        return True
    else:
        return False
