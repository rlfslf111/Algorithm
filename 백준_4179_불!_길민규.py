from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs():
    while jihun:
        if len(fire) > 0:
            for f in range(len(fire)):
                y, x = fire.popleft()
                for i in range(len(dy)):
                    fy, fx = y + dy[i], x + dx[i]
                    if fy < 0 or fy >= Y or fx < 0 or fx >= X or board[fy][fx] == '#':
                        continue
                    elif visit[fy][fx] == 0:
                        visit[fy][fx] = 4
                        fire.append((fy,fx))

        for j in range(len(jihun)):
            y, x, time = jihun.popleft()
            for i in range(len(dy)):
                jy, jx = y + dy[i], x + dx[i]
                if jy < 0 or jy >= Y or jx < 0 or jx >= X:
                    return time
                elif board[jy][jx] == '#' or board[jy][jx] == 'F':
                    continue
                elif visit[jy][jx] == 0:
                    visit[jy][jx] = 5
                    jihun.append((jy,jx,time+1))
    return 'IMPOSSIBLE'


Y, X = map(int,input().split())
visit = [[0]*X for _ in range(Y)]
board = []
jihun = deque()
fire = deque()
for i in range(Y):
    board.append(list(input()))
    for j in range(X):
        if board[i][j] == 'J':
            jihun.append((i,j,1))
            visit[i][j] = 5
        elif board[i][j] == 'F':
            fire.append((i,j))
            visit[i][j] = 4

print(bfs())