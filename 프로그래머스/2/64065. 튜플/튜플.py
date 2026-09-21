def solution(s):
    answer = []

    s = s[2:-2]

    sets = s.split("},{")

    sets = [list(map(int, x.split(","))) for x in sets]

    sets.sort(key=len)

    used = set()

    for nums in sets:
        for num in nums:
            if num not in used:
                answer.append(num)
                used.add(num)
                break

    return answer