S = input()
dat = [0] * 26
n = 0
i = 0
for s in S:
    dat[ord(s)-97] += 1

for d in dat:
    print(d, end= ' ')
