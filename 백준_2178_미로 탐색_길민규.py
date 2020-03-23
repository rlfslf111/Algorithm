from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs(y,x,cnt):
    q = deque()
    q.append((y,x,cnt))
    visit = [[0]*M for _ in range(N)]
    visit[y][x] = 1
    while q:
        y, x, cnt = q.popleft()
        if y == N-1 and x == M-1:
            print(cnt)
            break
        for i in range(len(dy)):
            ny, nx = y + dy[i], x+ dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M or visit[ny][nx] == 1:
                continue
            if maze[ny][nx] == 1:
                visit[ny][nx] = 1
                q.append((ny,nx,cnt+1))


N, M = map(int,input().split())
maze = [list(map(int,list(input()))) for _ in range(N)]

bfs(0,0,1)