from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    visit[y][x] = 1
    wolf_cnt = 0
    sheep_cnt = 0
    if board[y][x] == 'v':
        wolf_cnt += 1
    if board[y][x] == 'k':
        sheep_cnt += 1

    while q:
        y, x = q.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C or board[ny][nx] == '#':
                continue
            if board[ny][nx] == 'v' and visit[ny][nx] == 0:
                wolf_cnt += 1
                q.append((ny,nx))
                visit[ny][nx] = 1
            elif board[ny][nx] == 'k' and visit[ny][nx] == 0:
                sheep_cnt += 1
                visit[ny][nx] = 1
                q.append((ny,nx))
            elif board[ny][nx] == '.' and visit[ny][nx] == 0:
                q.append((ny,nx))
                visit[ny][nx] = 1

    if wolf_cnt >= sheep_cnt:
        wolf[0] += wolf_cnt
    else:
        sheep[0] += sheep_cnt


R, C = map(int,input().split())
visit = [[0] * C for _ in range(R)]
board = []
for i in range(R):
    board.append(list(input()))

wolf = [0]
sheep = [0]
for y in range(R):
    for x in range(C):
        if board[y][x] == '.' and visit[y][x] == 0:
            bfs(y,x)
        if board[y][x] == 'v' and visit[y][x] == 0:
            bfs(y,x)
        if board[y][x] == 'k' and visit[y][x] == 0:
            bfs(y,x)

print(sheep[0],wolf[0])
