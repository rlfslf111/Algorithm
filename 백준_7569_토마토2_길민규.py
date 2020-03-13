from collections import deque
dk = [-1,1]
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs():
    day = 0
    while q:
        k, y, x, d = q.popleft()
        for ud in range(len(dk)):
            nk = k + dk[ud]
            if nk < 0 or nk >= H or box[nk][y][x] != 0:
                continue
            if box[nk][y][x] == 0:
                box[nk][y][x] = 1
                q.append((nk,y,x,d+1))
                day = max(day,d+1)
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M or box[k][ny][nx] != 0:
                continue
            if box[k][ny][nx] == 0:
                box[k][ny][nx] = 1
                q.append((k,ny,nx,d+1))
                day = max(day,d+1)

    flag = True
    for k in range(H):
        for y in range(N):
            for x in range(M):
                if box[k][y][x] == 0:
                    flag = False
    if flag:
        return day
    else:
        return -1

M, N, H = map(int,input().split())
box = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
for k in range(H):
    for y in range(N):
        for x in range(M):
            if box[k][y][x] == 1:
                q.append((k,y,x,0))

print(bfs())
