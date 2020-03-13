import sys
sys.setrecursionlimit(1000000)

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def dfs(y,x):
    visit[y][x] = 1
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= Y or nx < 0 or nx >= X or visit[ny][nx] != 0:
            continue
        if board[ny][nx] == 0 and visit[ny][nx] == 0:
            visit[ny][nx] = 1
            cnt[0] += 1
            dfs(ny,nx)

Y, X, K = map(int,input().split())
board = [[0]*X for _ in range(Y)]
visit = [[0]*X for _ in range(Y)]

for k in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1

ans = []
cnt = [1]
lump = 0
for y in range(Y):
    for x in range(X):
        if board[y][x] == 0 and visit[y][x] != 1:
            dfs(y,x)
            ans.append(cnt[0])
            lump += 1
            cnt[0] = 1

ans.sort()
print(lump)
print(*ans)