from collections import Counter
def solution(k, tangerine):
    answer = 0
    total = 0
    cnt = Counter(tangerine)
    cnts = sorted(cnt.values(),reverse=True)
    for c in cnts:
        total += c
        answer += 1
        if total >= k:
            break
    return answer