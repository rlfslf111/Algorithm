import sys
sys.setrecursionlimit(10000000)

dy = [0,-1,0,1,0]
dx = [0,0,1,0,-1]
def dfs(y,x):
    for k in range(len(dy)):
        ny = y + dy[k]
        nx = x + dx[k]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if check[ny][nx] == i or location[ny][nx] == i:
            continue
        if check[ny][nx] != i:
            check[ny][nx] = i
            dfs(ny,nx)

N = int(input())
location = [list(map(int,input().split())) for _ in range(N)]
max_height = max(max(location))

ans =[1]
for i in range(0,max_height):
    for y1 in range(N):
        for x1 in range(N):
            if location[y1][x1] <= i:
                location[y1][x1] = i

    check = [[0]*N for _ in range(N)]

    cnt = 0
    for y2 in range(N):
        for x2 in range(N):
            if location[y2][x2] > i and check[y2][x2] != i:
                dfs(y2,x2)
                cnt += 1
    ans.append(cnt)
print(max(ans))