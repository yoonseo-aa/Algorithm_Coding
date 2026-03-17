N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

xs = set()
ys = set()

for x, y, w, h in arr:
    xs.add(x)
    xs.add(x + w)
    ys.add(y)
    ys.add(y + h)

xs = sorted(xs)
ys = sorted(ys)

x_id = {x: i for i, x in enumerate(xs)}
y_id = {y: i for i, y in enumerate(ys)}

board = [[0] * (len(ys) - 1) for _ in range(len(xs) - 1)]

for n in range(N):
    x, y, w, h = arr[n]
    for i in range(x_id[x], x_id[x + w]):
        for j in range(y_id[y], y_id[y + h]):
            board[i][j] = n + 1

dic = {}

for i in range(len(xs) - 1):
    for j in range(len(ys) - 1):
        k = board[i][j]
        if k == 0:
            continue
        area = (xs[i + 1] - xs[i]) * (ys[j + 1] - ys[j])
        dic[k] = dic.get(k, 0) + area

for i in range(1, N + 1):
    print(dic.get(i, 0))
