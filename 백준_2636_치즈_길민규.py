import sys
sys.setrecursionlimit(1000000)

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def dfs(y,x):
    visit[y][x] = 1
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= Y or nx < 0 or nx >= X or visit[ny][nx] == 7:
            continue
        if board[ny][nx] == 1:
            board[ny][nx] = 2
            return
        if board[ny][nx] == 0 and visit[ny][nx] == 0:
            visit[ny][nx] = 7
            dfs(ny,nx)


Y, X = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(Y)]
visit = [[0]*X for _ in range(Y)]
remain = []


while 1:
    # 2로 변경된 테두리를 모두 없애고 1의 갯수를 센다
    cnt_c = 0
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 2:
                board[y][x] = 0
            if board[y][x] == 1:
                cnt_c += 1
    remain.append(cnt_c)

    # 테두리 선별해서 테두리를 모두 2로 변경
    for i in range(X):
        if board[0][i] == 0:
            dfs(0,i)
            visit = [[0] * X for _ in range(Y)]
        if board[Y-1][i] == 0:
            dfs(Y-1,i)
            visit = [[0] * X for _ in range(Y)]
    for j in range(Y):
        if board[j][0] == 0:
            dfs(j,0)
            visit = [[0] * X for _ in range(Y)]
        if board[j][X-1] == 0:
            dfs(j,X-1)
            visit = [[0] * X for _ in range(Y)]

    cnt_z = 0
    for y in range(Y):
        cnt_z += board[y].count(0)
    if cnt_z == Y*X:
        break

print(len(remain)-1)
print(remain[len(remain)-2])