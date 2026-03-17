import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    text = list(input())
    result = []
    valid = False
    for i in range(len(text)):
        if text[i] == '(':
            result.append(text[i])
        elif text[i] == ')':
            if result:
                result.pop()
            else:
                valid = True
                break

    if result or valid:
        print('NO')
    else:
        print('YES')