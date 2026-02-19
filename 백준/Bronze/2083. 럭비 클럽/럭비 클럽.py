import sys
input = sys.stdin.readline

while True:
    arr = input().split()
    
    if arr[0] == '#' and arr[1] == '0' and arr[2] == '0':
        break
    
    name = arr[0]
    age = int(arr[1])
    weight = int(arr[2])
    
    if age > 17 or weight >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')
