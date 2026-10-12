def solution(s):
    res = ''
    arr = s.split(' ')

    for ar in arr:
        if ar:
            res += ar[0].upper() + ar[1:].lower()
        res += ' '

    return res[:-1]