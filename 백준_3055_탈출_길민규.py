from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs():
    while hog:

        # 물이 범람하는 경우 (사방으로 모두 범람시킨 후 고슴도치 이동)
        if len(water) > 0:
            for k in range(len(water)):
                wy, wx = water.popleft()
                for i in range(len(dy)):
                    ty, tx = wy + dy[i], wx + dx[i]
                    if ty < 0 or ty >= R or tx < 0 or tx >= C or forest[ty][tx] == 'D' or forest[ty][tx] == 'X':
                        continue
                    if forest[ty][tx] == '.' and visit[ty][tx] == 0:
                        water.append((ty,tx))
                        visit[ty][tx] = 7

        # 물이 사방으로 범람이 이루어진 후 고슴도치 이동, 이동 경로를 사방으로 모두 표현
        for k in range(len(hog)):
            hy, hx, time = hog.popleft()
            for i in range(len(dy)):
                ny, nx = hy + dy[i], hx + dx[i]
                if ny < 0 or ny >= R or nx < 0 or nx >= C or forest[ny][nx] == 'X':
                    continue
                if forest[ny][nx] == 'D':
                    return time
                if forest[ny][nx] == '.' and visit[ny][nx] == 0:
                    hog.append((ny,nx,time + 1))
                    visit[ny][nx] = 3

    return 'KAKTUS'

R, C = map(int,input().split())
visit = [[0]*C for _ in range(R)]
water = deque()
hog = deque()

forest = []
for i in range(R):
    forest.append(list(input()))
    for j in range(C):
        if forest[i][j] == '*':
            water.append((i,j))
            visit[i][j] = 7
        elif forest[i][j] == 'S':
            hog.append((i,j,1))
            visit[i][j] = 3

print(bfs())