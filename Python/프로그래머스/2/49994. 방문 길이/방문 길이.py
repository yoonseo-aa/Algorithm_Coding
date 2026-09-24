def solution(dirs):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = set()
    res = 0
    direction = {
        'U' : 0,
        'D' : 1,
        'R' : 2,
        'L' : 3
    }
    x, y = 0, 0 
    for d in dirs:
        # 방향 찾기
        i = direction[d]
        # nx, ny 계산
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 검사
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 길 검사
            if (x,y,nx,ny) not in visited:
                res += 1
                visited.add((x,y,nx,ny))
                visited.add((nx,ny,x,y))
                # x, y 갱신
            x, y = nx, ny
    return res