def solution(elements):
    answer = set()
    
    arr = elements + elements
    
    n = len(elements)
    
    for length in range(1, n + 1):
        for start in range(n):
            total = sum(arr[start:start + length])
            answer.add(total)
    
    return len(answer)