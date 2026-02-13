a = [list(map(int, input().split())) for _ in range(9)]
max_v = float('-inf')
idx_arr = []
for i in range(9):
    for j in range(9):
        if a[i][j] > max_v:
            max_v = a[i][j]      
            idx_arr= [i+1,j+1]       
print(max_v)                  
print(*idx_arr)