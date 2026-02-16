N = int(input())

max_len = 0
max_seq = []

for second in range(1, N + 1):
    seq = [N, second]

    while True:
        next_num = seq[-2] - seq[-1]
        if next_num < 0:
            break
        seq.append(next_num)

    if len(seq) > max_len:
        max_len = len(seq)
        max_seq = seq

print(max_len)
print(*max_seq)
