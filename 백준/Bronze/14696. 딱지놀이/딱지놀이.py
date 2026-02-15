N = int(input())

for _ in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    A = a[1:]
    B = b[1:]

    for shape in [4, 3, 2, 1]:
        if A.count(shape) > B.count(shape):
            print('A')
            break
        elif A.count(shape) < B.count(shape):
            print('B')
            break
    else:
        print('D')
