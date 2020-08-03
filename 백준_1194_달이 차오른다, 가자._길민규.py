import sys
input = sys.stdin.readline
from collections import deque

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
g_alphbet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs():
    while minsik:
        y,x,z = minsik.popleft()
        if board[y][x] == '1':
            return go[y][x][z] - 1
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M or board[ny][nx] == '#':
                continue
            if go[ny][nx][z] == 0:
                if board[ny][nx] in alphabet:
                    nz = z | (1 << (ord(board[ny][nx]) - ord('a')))
                    if go[ny][nx][nz] == 0:
                        go[ny][nx][nz] = go[y][x][z] + 1
                        minsik.append((ny,nx,nz))
                elif board[ny][nx] in g_alphbet:
                    if z & (1 << (ord(board[ny][nx]) - ord('A'))):
                        go[ny][nx][z] = go[y][x][z] + 1
                        minsik.append((ny,nx,z))
                else:
                    go[ny][nx][z] = go[y][x][z] + 1
                    minsik.append((ny,nx,z))

    return -1

N, M = map(int,input().split())
board = []
go = [[[0 for _ in range(64)] for _ in range(M)] for _ in range(N)]
minsik = deque()
for i in range(N):
    board.append(list(input().strip()))
    for j in range(M):
        if board[i][j] == '0':
            minsik.append((i,j,0))
            go[i][j][0] = 1

print(bfs())
