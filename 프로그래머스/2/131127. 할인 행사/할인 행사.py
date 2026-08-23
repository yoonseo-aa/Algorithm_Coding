def solution(want, number, discount):
    answer = 0
    
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    window = {}
    for i in range(10):
        window[discount[i]] = window.get(discount[i], 0) + 1
    
    for i in range(10, len(discount) + 1):
        
        if window == want_dict:
            answer += 1
        
        if i == len(discount):
            break
        
        old = discount[i - 10]
        window[old] -= 1
        
        if window[old] == 0:
            del window[old]
        
        new = discount[i]
        window[new] = window.get(new, 0) + 1
    
    return answer