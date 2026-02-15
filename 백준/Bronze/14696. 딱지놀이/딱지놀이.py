N = int(input())

for _ in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if a[0] != b[0] and a[1:].count(4) != b[1:].count(4):
        if a[1:].count(4) > b[1:].count(4):
            print('A')
        else:
            print('B')
    elif a[1:].count(3) != b[1:].count(3):
        if a[1:].count(3) < b[1:].count(3):
            print('B')
        else:
            print('A')
    elif a[1:].count(2) != b[1:].count(2):
        if a[1:].count(2) < b[1:].count(2):
            print('B')
        else:
            print('A')
    elif a[1:].count(1) != b[1:].count(1):
        if a[1:].count(1) < b[1:].count(1):
            print('B')
        else:
            print('A')
    else:
        print('D')
