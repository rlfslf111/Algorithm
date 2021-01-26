from collections import deque

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def go(y,x):
    find = deque()
    find.append((y,x,0))
    check[y][x] = 1
    dis = 0

    while find:
        i,j,d = find.popleft()
        for k in range(len(dy)):
            ny, nx = i + dy[k], j + dx[k]
            if ny < 0 or ny >= Y or nx < 0 or nx >= X:
                continue
            elif island[ny][nx] == 'W' or check[ny][nx] == 1:
                continue
            else:
                check[ny][nx] = 1
                find.append((ny,nx,d+1))
                dis = max(dis,d+1)

    return dis



Y,X = map(int,input().split())
island = [input() for _ in range(Y)]
ans = 0

for i in range(Y):
    for j in range(X):
        if island[i][j] == 'L':
            check = [[0]*X for _ in range(Y)]
            ans = max(ans,go(i,j))

print(ans)