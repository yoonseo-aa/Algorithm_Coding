def solution(arr):
    answer = [arr[0]]
    pre = arr[0]
    for i in range(len(arr)):
        if pre != arr[i]:
            answer.append(arr[i])
        pre = arr[i]
    return answer