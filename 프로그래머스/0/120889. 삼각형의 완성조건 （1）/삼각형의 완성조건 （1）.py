def solution(sides):
    max_num = max(sides)
    if sum(sides)-max_num > max_num:
        return 1
    else:
        return 2
