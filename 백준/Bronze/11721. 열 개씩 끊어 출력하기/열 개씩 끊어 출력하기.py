text = input()
if len(text) % 10 == 0: repeat = len(text) // 10
else: repeat = (len(text) // 10) + 1
start = 0
end = 10
for i in range(repeat):
    print(text[start:end])
    start = end
    end = start + 10
    if i == repeat-1: end = start + len(text) % 10
