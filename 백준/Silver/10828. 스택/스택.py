stack = []

def push(stack, item):
    stack.append(item)
    return stack

def pop_stack(stack):
    if stack: return stack.pop()
    return -1

N = int(input())

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push': push(stack, int(cmd[1]))
    elif cmd[0] == 'pop': print(pop_stack(stack))
    elif cmd[0] == 'top':
        if len(stack) == 0: print(-1)
        else : print(stack[-1])
    elif cmd[0] == 'size': print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
