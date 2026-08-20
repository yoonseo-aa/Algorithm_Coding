def solution(n, words):
    used = set()
    turn = 0
    for i in range(len(words)):
        if i > 0 and words[i][0] != words[i-1][-1]:
            return [i % n + 1, i // n + 1]
        if words[i] in used:
            return [i % n + 1, i // n + 1]
            
        used.add(words[i])
    return [0,0]