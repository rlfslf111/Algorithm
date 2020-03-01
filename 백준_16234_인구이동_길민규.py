import sys
sys.setrecursionlimit(10000000)

dy = [0,-1,0,1,0]
dx = [0,0,1,0,-1]
def open_(y,x):
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or boundary[ny][nx] or visit[ny][nx]:
            continue
        if L <= abs(world[y][x] - world[ny][nx]) <= R:
            visit[ny][nx] = 1
            person[0] += world[ny][nx]
            peninsula[0] += 1
            boundary[ny][nx] = True
            open_(ny,nx)

def move(y,x):
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or boundary[ny][nx] == False:
            continue
        if boundary[ny][nx]:
            world[ny][nx] = person[0]
            boundary[ny][nx] = False
            move(ny,nx)


N, L, R = map(int,input().split())
world = [list(map(int,input().split())) for _ in range(N)]

boundary = [[False]*N for _ in range(N)]
visit = [[0]*N for _ in range(N)]

person = [0]
peninsula = [0]
cnt = 0
flag = [True]

while flag[0]:
    for y in range(N):
        for x in range(N):
            if visit[y][x]:
                continue
            if not boundary[y][x]:
                open_(y,x)
            if boundary[y][x]:
                person[0] //= peninsula[0]
                move(y,x)
            person[0] = 0
            peninsula[0] = 0
    flag[0] = False
    for y in range(N):
        if 1 in visit[y]:
            flag[0] = True
            cnt += 1
            break
    visit = [[0] * N for _ in range(N)]

print(cnt)