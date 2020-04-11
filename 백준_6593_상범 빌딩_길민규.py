import sys
sys.stdin = open('input.txt','r')

from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]
dk = [-1,1]
def bfs(k,y,x):
    q = deque()
    q.append((k,y,x,0))
    visit = [[[0]*C for _ in range(R)]for _ in range(L)]
    visit[k][y][x] = 1

    while q:
        k,y,x,d = q.popleft()
        if board[k][y][x] == 'E':
            return 'Escaped in {} minute(s).'.format(d)
        for i in range(len(dk)):
            nk = k + dk[i]
            if nk < 0 or nk >= L or board[nk][y][x] == '#':
                continue
            if visit[nk][y][x] == 0:
                visit[nk][y][x] = 1
                q.append((nk,y,x,d+1))

        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C or board[k][ny][nx] == '#':
                continue
            if visit[k][ny][nx] == 0:
                visit[k][ny][nx] = 1
                q.append((k,ny,nx,d+1))
    return 'Trapped!'

while 1:
    L, R, C = map(int,input().split())
    if L == 0 and R == 0 and C == 0:
        break
    else:
        board = [[] for _ in range(L)]
        for l in range(L):
            for r in range(R):
                board[l].append(list(input()))
            ip = input()

        for k in range(L):
            for y in range(R):
                for x in range(C):
                    if board[k][y][x] == 'S':
                        print(bfs(k,y,x))