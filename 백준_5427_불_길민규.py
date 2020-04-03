from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs():
    while sang:
        if len(fire) > 0:
            for k in range(len(fire)):
                fy, fx = fire.popleft()
                for i in range(len(dy)):
                    ty, tx = fy + dy[i], fx + dx[i]
                    if ty < 0 or ty >= h or tx < 0 or tx >= w or building[ty][tx] == '#':
                        continue
                    if building[ty][tx] == '.' and visit[ty][tx] == 0:
                        visit[ty][tx] = 4
                        fire.append((ty,tx))

        for k in range(len(sang)):
            y, x, time = sang.popleft()
            for i in range(len(dy)):
                ny, nx = y + dy[i], x + dx[i]
                if ny < 0 or ny >= h or nx < 0 or nx >= w:
                    return time
                if building[ny][nx] == '#' or building[ny][nx] == '*':
                    continue
                if building[ny][nx] == '.' and visit[ny][nx] == 0:
                    visit[ny][nx] = 7
                    sang.append((ny,nx,time + 1))

    return 'IMPOSSIBLE'


for t in range(1,int(input())+1):
    w, h = map(int,input().split())
    fire = deque()
    sang = deque()
    visit = [[0]*w for _ in range(h)]
    building = []
    for i in range(h):
        building.append(list(input()))
        for j in range(w):
            if building[i][j] == '*':
                fire.append((i,j))
                visit[i][j] = 4
            elif building[i][j] == '@':
                sang.append((i,j,1))
                visit[i][j] = 7

    print(bfs())