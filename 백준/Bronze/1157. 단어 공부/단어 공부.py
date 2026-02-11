text = input().upper()
arr = [0] * 26   # A~Z만 사용

for t in text:
    arr[ord(t) - ord('A')] += 1

max_v = max(arr)

if arr.count(max_v) > 1:
    print('?')
else:
    print(chr(arr.index(max_v) + ord('A')))
