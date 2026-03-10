doc = input()
word = input()

n = len(word)

cnt = 0
i = 0
while True:
    if doc[i:i+n] == word:
        cnt += 1
        i = i + n
        continue
    i += 1
    if i + n > len(doc):
        break

print(cnt)
