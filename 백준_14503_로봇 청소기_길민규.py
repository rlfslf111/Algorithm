def clean(y,x,dir):
    global cnt
    board[y][x] = 2

    current_y = y
    current_x = x

    if dir == 0:
        change_dir = [3,2,1,0]
        dy = [0, 1, 0, -1]
        dx = [-1, 0, 1, 0]
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M or board[ny][nx] != 0:
                continue
            if board[ny][nx] == 0:
                board[ny][nx] = 2
                dir = change_dir[i]
                y, x = ny, nx
                cnt += 1
                return clean(y,x,dir)
        current_y = y + dy[1]
        current_x = x + dx[1]
        if 0 <= current_y < N and 0 <= current_x < M and board[current_y][current_x] != 1:
            clean(current_y,current_x,dir)
        return

    if dir == 1:
        change_dir = [0,3,2,1]
        dy = [-1,0,1,0]
        dx = [0,-1,0,1]
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M or board[ny][nx] != 0:
                continue
            if board[ny][nx] == 0:
                board[ny][nx] = 2
                dir = change_dir[i]
                y, x = ny, nx
                cnt += 1
                return clean(y,x,dir)
        current_y = y + dy[1]
        current_x = x + dx[1]
        if 0 <= current_y < N and 0 <= current_x < M and board[current_y][current_x] != 1:
            clean(current_y, current_x, dir)
        return

    if dir == 2:
        change_dir = [1,0,3,2]
        dy = [0,-1,0,1]
        dx = [1,0,-1,0]
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M or board[ny][nx] != 0:
                continue
            if board[ny][nx] == 0:
                board[ny][nx] = 2
                dir = change_dir[i]
                y, x = ny, nx
                cnt += 1
                return clean(y,x,dir)
        current_y = y + dy[1]
        current_x = x + dx[1]
        if 0 <= current_y < N and 0 <= current_x < M and board[current_y][current_x] != 1:
            clean(current_y, current_x, dir)
        return

    if dir == 3:
        change_dir = [2,1,0,3]
        dy = [1,0,-1,0]
        dx = [0,1,0,-1]
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M or board[ny][nx] != 0:
                continue
            if board[ny][nx] == 0:
                board[ny][nx] = 2
                dir = change_dir[i]
                y, x = ny, nx
                cnt += 1
                return clean(y,x,dir)
        current_y = y + dy[1]
        current_x = x + dx[1]
        if 0 <= current_y < N and 0 <= current_x < M and board[current_y][current_x] != 1:
            clean(current_y, current_x, dir)
        return

N, M = map(int,input().split())
r, c, dir = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
cnt = 1
clean(r,c,dir)
print(cnt)
