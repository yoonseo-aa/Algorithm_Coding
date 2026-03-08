alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

i = 0
cnt = 0

while i < len(word):
    if word[i:i+3] == 'dz=':
        cnt += 1
        i += 3
    elif word[i:i+2] in alpa:
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1

print(cnt)