def solution(clothes):
    answer = 1
    clothes_hash = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in clothes_hash: 
            clothes_hash[clothes[i][1]] = 1
        else:
            clothes_hash[clothes[i][1]] += 1
    
    for cnt in clothes_hash.values():
        answer *= cnt+1
    return answer-1