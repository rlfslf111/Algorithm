from collections import deque

dy = [1,0,-1,0]
dx = [0,1,0,-1]
def find(y,x):
    q = deque()
    q.append((y,x,0))
    check[y][x] = True
    distance = 0
    while q:
        y,x,d = q.popleft()
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0  or nx >= X or ny < 0 or ny >= Y:
                continue
            if check[ny][nx] == False and map[ny][nx] == 'L':
                q.append((ny,nx,d+1))
                check[ny][nx] = True
                distance = max(distance,d+1)
    return distance

Y, X = map(int,input().split())
map = [input() for _ in range(Y)]

ans = 0
for y in range(Y):
    for x in range(X):
        if map[y][x] == 'L':
            check = [[False]*X for _ in range(Y)]
            ans = max(ans,find(y,x))
print(ans)






