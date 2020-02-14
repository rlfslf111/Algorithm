import sys
sys.stdin = open('cabbage.txt','r')

import sys
sys.setrecursionlimit(100000)
dy = [0,0,-1,1]
dx = [1,-1,0,0]
def worm(y,x):
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if field[ny][nx] == 1:
            field[ny][nx] = 0
            worm(ny,nx)


tc = int(input())
for t in range(tc):
    M, N, gesu = map(int,input().split())

    field = [[0]*M for _ in range(N)]

    for g in range(gesu):
        x_cabbage, y_cabbage = map(int,input().split())
        field[y_cabbage][x_cabbage] = 1

    cnt = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:
                worm(y,x)
                cnt += 1
    print(cnt)


