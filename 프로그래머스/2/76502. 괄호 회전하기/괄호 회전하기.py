def solution(s):
    answer = 0

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for x in range(len(s)):
        rotated = s[x:] + s[:x]
        stack = []

        for bracket in rotated:
            if bracket in '([{':
                stack.append(bracket)

            else:
                if not stack or stack[-1] != pairs[bracket]:
                    break

                stack.pop()

        else:
            if not stack:
                answer += 1

    return answer