import sys
r = sys.stdin.readline
from collections import deque

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

H, W = map(int,r().split())

col = deque()
castle = []
for i in range(H):
    castle.append(list(r()))
    for j in range(W):
        if castle[i][j] == '.':
            col.append((i,j))
            castle[i][j] = -1
        else:
            castle[i][j] = int(castle[i][j])

time = 0
while col:
    # 처음 바닥의 좌표 만큼만 반복
    for _ in range(len(col)):
        y, x = col.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= H or nx < 0 or nx >= W or castle[ny][nx] == -1:
                continue
            castle[ny][nx] -= 1
            if castle[ny][nx] == 0:
                castle[ny][nx] = -1
                col.append((ny,nx))
    time += 1

print(time-1)