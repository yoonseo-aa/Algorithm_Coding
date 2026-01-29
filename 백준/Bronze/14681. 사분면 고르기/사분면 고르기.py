x = int(input())
y = int(input())
def quadrant(num1,num2):
    if num1 > 0 and num2 > 0:
        return 1
    elif num1 < 0 and num2 > 0:
        return 2
    elif num1 < 0 and num2 < 0:
        return 3
    else:
        return 4
    
result = quadrant(x,y)
print(result)