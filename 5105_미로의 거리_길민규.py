from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs():
    while q:
        y, x, d = q.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N or visit[ny][nx] != 0 or maze[ny][nx] == 1:
                continue
            if maze[ny][nx] == 3:
                return d
            if maze[ny][nx] == 0 and visit[ny][nx] == 0:
                q.append((ny,nx,d+1))
                visit[ny][nx] = 1
    return 0

for t in range(1,int(input())+1):
    N = int(input())
    visit = [[0]*N for _ in range(N)]
    q = deque()
    maze = []
    for i in range(N):
        maze.append(list(map(int,list(input()))))
        for j in range(N):
            if maze[i][j] == 2:
                visit[i][j] = 1
                q.append((i,j,0))

    print('#{} {}'.format(t,bfs()))
