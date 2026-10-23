from collections import Counter

def solution(weights):
    count = Counter(weights)
    answer = 0

    for w, cnt in count.items():
        answer += cnt * (cnt - 1) // 2

        answer += cnt * count[w * 2]

        if w % 2 == 0:
            answer += cnt * count[w * 3 // 2]
        if w % 3 == 0:
            answer += cnt * count[w * 4 // 3]

    return answer