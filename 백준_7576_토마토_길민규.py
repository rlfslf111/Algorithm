from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs():
    day = 0
    while q:
        y, x, d = q.popleft()
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= Y or nx < 0 or nx >= X or box[ny][nx] != 0:
                continue
            if box[ny][nx] == 0:
                q.append((ny,nx,d+1))
                box[ny][nx] = 1
                day = max(day,d+1)
    flag = True
    for i in range(Y):
        for j in range(X):
            if box[i][j] == 0:
                flag = False
    if flag:
        return day
    else:
        return -1


X, Y = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(Y)]

q = deque()

for y in range(Y):
    for x in range(X):
        if box[y][x] == 1:
            q.append((y,x,0))
print(bfs())
