def solution(numbers):
    answer = []

    for number in numbers:
        binary = bin(number)[2:]

        size = 1

        while size < len(binary):
            size = size * 2 + 1

        binary = binary.zfill(size)

        if check(binary):
            answer.append(1)
        else:
            answer.append(0)

    return answer


def check(tree):
    if len(tree) == 1:
        return True

    mid = len(tree) // 2

    left = tree[:mid]
    right = tree[mid + 1:]

    if tree[mid] == '0':
        if '1' in left or '1' in right:
            return False

    return check(left) and check(right)