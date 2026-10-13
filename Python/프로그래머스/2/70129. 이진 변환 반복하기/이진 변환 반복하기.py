def solution(s):
    answer = []
    cnt, zero_cnt = 0, 0
    while len(s) != 1:
        zero_cnt += s.count("0")
        s = s.replace("0","")
        length = len(s)
        s = bin(length)[2:]
        cnt += 1
    return [cnt, zero_cnt]