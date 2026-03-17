import sys
from collections import deque

input = sys.stdin.readline
N = int(input())



def push(stack,n):
    stack.append(n)

def front(stack):
    if stack:
        return stack[0]
    else:
        return -1

def back(stack):
    if stack:
        return stack[-1]
    else:
        return -1

def size(stack):
    return len(stack)

def pop(stack):
    if stack:
        return stack.popleft()
    else:
        return -1

def is_empty(stack):
    if stack:
        return 0
    else:
        return 1

stack = deque()

for _ in range(N):
    command = input().split()
    if len(command) > 1:
        if command[0] == 'push':
            push(stack, command[1])
    else:
        if command[0] == 'pop':
            print(pop(stack))
        elif command[0] == 'front':
            print(front(stack))
        elif command[0] == 'size':
            print(size(stack))
        elif command[0] == 'back':
            print(back(stack))
        elif command[0] == 'empty':
            print(is_empty(stack))