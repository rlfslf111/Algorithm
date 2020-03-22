from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs(y,x):
    q = deque()
    q.append((y,x))
    visit[y][x] = 1
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < Y and 0 <= nx < X and board[ny][nx] == 0 and visit[ny][nx] == 0:
                q.append((ny,nx))
                cnt += 1
                visit[ny][nx] = 1

    area.append(cnt)

Y, X, K = map(int,input().split())
board = [[0]*X for _ in range(Y)]
visit = [[0]*X for _ in range(Y)]

for k in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            board[i][j] = 1

lump = 0
area = []
for y in range(Y):
    for x in range(X):
        if board[y][x] == 0 and visit[y][x] == 0:
            bfs(y,x)
            lump += 1
            
area.sort()
print(lump)
print(*area)
