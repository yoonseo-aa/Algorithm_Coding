def solution(topping):
    n = len(topping)

    left = [0] * n
    right = [0] * n

    s = set()
    for i in range(n):
        s.add(topping[i])
        left[i] = len(s)

    s = set()
    for i in range(n - 1, -1, -1):
        s.add(topping[i])
        right[i] = len(s)

    answer = 0

    for i in range(n - 1):
        if left[i] == right[i + 1]:
            answer += 1

    return answer