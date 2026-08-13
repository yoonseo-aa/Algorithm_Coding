def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        a = answer
        b = arr[i]

        while b:
            a, b = b, a % b

        answer = answer * arr[i] // a

    return answer