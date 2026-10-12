def solution(s):
    arr = list(map(int,s.split()))
    res = str(min(arr)) + " " + str(max(arr))
    return res