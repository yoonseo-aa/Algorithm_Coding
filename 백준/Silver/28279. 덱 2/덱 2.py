from collections import deque
import sys

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if len(command) > 2:
        a, b = map(int, command.split())
    else:
        a = int(command)
    if a == 1:
        q.appendleft(b)
    elif a == 2:
        q.append(b)
    elif a == 3:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif a == 4:
        if q:
            print(q.pop())
        else:
            print(-1)
    elif a == 5:
        print(len(q))
    elif a == 6:
        if q:
            print(0)
        else:
            print(1)
    elif a == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    elif a == 8:
        if q:
            print(q[-1])
        else:
            print(-1)

