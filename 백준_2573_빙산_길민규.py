from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]
def Lump(y,x):
    q = deque()
    q.append((y,x))
    while q:
        ty, tx = q.popleft()
        for i in range(len(dy)):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or ny >= Y or nx < 0 or nx >= X or visit[ny][nx] == 1:
                continue
            if glacier[ny][nx] != 0 and visit[ny][nx] == 0:
                q.append((ny,nx))
                visit[ny][nx] = 1


Y, X = map(int,input().split())
glacier = [list(map(int,input().split())) for _ in range(Y)]

visit = [[0]*X for _ in range(Y)]
melt = [[0]*X for _ in range(Y)]

tmp = 0
step = 0
while tmp < 2:
    step += 1
    # 빙산이 다 녹을때까지 분리가 안됐을 경우
    cnt = 0
    for y in range(Y):
        cnt += glacier[y].count(0)
    if cnt == Y*X:
        step = 0
        break

    # 빙산 녹이기
    for y in range(Y):
        for x in range(X):
            if glacier[y][x] != 0:
                cnt_z = 0
                for i in range(len(dy)):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= Y or nx < 0 or nx >= X:
                        continue
                    if glacier[ny][nx] == 0:
                        cnt_z += 1
                melt[y][x] = cnt_z

    for y in range(Y):
        for x in range(X):
            if glacier[y][x] != 0:
                glacier[y][x] -= melt[y][x]
                melt[y][x] = 0
                if glacier[y][x] < 0:
                    glacier[y][x] = 0

    # 몇덩어리인지 센다
    lump = 0
    for y in range(Y):
        for x in range(X):
            if glacier[y][x] != 0 and visit[y][x] != 1:
                Lump(y, x)
                lump += 1
    visit = [[0] * X for _ in range(Y)]
    tmp = lump

print(step)