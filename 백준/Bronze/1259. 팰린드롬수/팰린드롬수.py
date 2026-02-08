while True:
    num = input()
    arr = list(num)
    if int(num) == 0: break
    if num == num[::-1]: print('yes')
    else: print('no')