def solution(n):
    answer = ''
    num_list = list(map(int, str(n)))
    num_list.sort(reverse=True)
    for i in range(len(num_list)):
        answer += str(num_list[i])
    return int(answer)