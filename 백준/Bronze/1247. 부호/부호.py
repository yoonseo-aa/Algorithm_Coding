import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input().strip())
    result = 0

    for _ in range(N):
        result += int(input().strip())

    if result == 0:
        print("0")
    elif result > 0:
        print("+")
    else:
        print("-")
