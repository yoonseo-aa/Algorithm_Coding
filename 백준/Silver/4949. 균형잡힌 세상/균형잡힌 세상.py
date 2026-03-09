while True:
    sen = input()

    if sen == '.':
        break

    stack = []
    flag = True

    for s in sen:
        if s == '(' or s == '[':
            stack.append(s)

        elif s == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            stack.pop()

        elif s == ']':
            if not stack or stack[-1] != '[':
                flag = False
                break
            stack.pop()

    if flag and not stack:
        print('yes')
    else:
        print('no')