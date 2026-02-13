A, B = input().split()

if int(A[::-1]) < int(B[::-1]):
    print(B[::-1])
else:
    print(A[::-1])

