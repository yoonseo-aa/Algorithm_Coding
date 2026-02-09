import sys
input = sys.stdin.readline

stack = []
out = []

N = int(input())

for _ in range(N):
    cmd = input().split()

    if cmd[0] == '1':          # push
        stack.append(cmd[1])

    elif cmd[0] == '2':        # pop
        if stack:
            out.append(stack.pop())
        else:
            out.append('-1')

    elif cmd[0] == '3':        # size
        out.append(str(len(stack)))

    elif cmd[0] == '4':        # empty
        out.append('1' if not stack else '0')

    elif cmd[0] == '5':        # top
        if stack:
            out.append(stack[-1])
        else:
            out.append('-1')

print('\n'.join(out))
