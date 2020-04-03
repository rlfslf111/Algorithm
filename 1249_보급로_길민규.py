from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    visit = [[1231231]*N for _ in range(N)]
    visit[y][x] = road[y][x]
    while q:
        y, x = q.popleft()
        count = visit[y][x]
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if count + road[ny][nx] < visit[ny][nx]:
                visit[ny][nx] = count + road[ny][nx]
                q.append((ny,nx))

    return visit[N-1][N-1]

for t in range(1,int(input())+1):
    N = int(input())
    road = [list(map(int,list(input()))) for _ in range(N)]

    print('#{} {}'.format(t,bfs(0,0)))
