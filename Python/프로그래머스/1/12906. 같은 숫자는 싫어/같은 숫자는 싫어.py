def solution(arr):
    stack = []
    
    for a in arr:
        if not stack:
            stack.append(a)
        if stack[-1] == a:
            continue
        stack.append(a)
    
    
    return stack