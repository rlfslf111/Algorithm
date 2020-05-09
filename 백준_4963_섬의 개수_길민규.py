from collections import deque

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    visit[y][x] = 1

    while q:
        y, x = q.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            elif board[ny][nx] == 1 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                q.append((ny,nx))

while 1:
    w, h = map(int,input().split())
    if h == 0 or w == 0:
        break
    visit = [[0]*w for _ in range(h)]
    board = [list(map(int,input().split())) for _ in range(h)]

    island = 0

    for y in range(h):
        for x in range(w):
            if board[y][x] == 1 and visit[y][x] == 0:
                bfs(y,x)
                island += 1
    print(island)