def solution(price, money, count):
    m = 0
    for i in range(1,count+1):
        m += price*i
    answer = m - money
    if answer < 0 : answer = 0
    return answer