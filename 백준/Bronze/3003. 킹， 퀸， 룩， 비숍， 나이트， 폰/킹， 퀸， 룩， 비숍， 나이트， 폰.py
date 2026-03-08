correct = [1,1,2,2,2,8]
pieces = list(map(int,input().split()))

print(*(c-p for c,p in zip(correct,pieces)))