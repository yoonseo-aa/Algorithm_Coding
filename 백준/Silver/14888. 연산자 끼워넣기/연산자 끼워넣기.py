N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

def dfs(idx, result):
    global max_v, min_v

    if idx == N:
        max_v = max(max_v, result)
        min_v = min(min_v, result)
        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            if i == 0:
                dfs(idx + 1, result + arr[idx])
            elif i == 1:
                dfs(idx + 1, result - arr[idx])
            elif i == 2:
                dfs(idx + 1, result * arr[idx])
            elif i == 3:
                dfs(idx + 1, int(result / arr[idx]))
            op[i] += 1


max_v = float('-inf')
min_v = float('inf')

dfs(1, arr[0])

print(max_v)
print(min_v)