T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    r1, r2 = max(r1, r2), min(r1, r2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)

    if distance == 0 and r1 == r2:
        print(-1)
    elif r1 + r2 < distance:
        print(0)
    elif r1 - r2 > distance:
        print(0)
    elif r1 + r2 == distance:
        print(1)
    elif r1 - r2 == distance:
        print(1)
    elif r1 - r2 < distance < r1 + r2:
        print(2)