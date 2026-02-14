arr = ['','','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

text = input()
res = 0
for t in text:
    for i in range(2,len(arr)):
        n = arr[i].find(t)
        if n != -1:
            res += i

print(res)