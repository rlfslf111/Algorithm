from collections import deque
dy = [-2,-1,1,2,2,1,-1,-2]
dx = [1,2,2,1,-1,-2,-2,-1]
def bfs():
    while Q:
        y, x = Q.popleft()
        if y == end_y and x == end_x:
            return visit[y][x]
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if not visit[ny][nx]:
                visit[ny][nx] = visit[y][x] + 1
                Q.append([ny,nx])


for t in range(int(input())):
    N = int(input())
    cur_y, cur_x = map(int,input().split())
    end_y, end_x = map(int,input().split())
    visit = [[0]*N for _ in range(N)]
    Q = deque()
    Q.append([cur_y,cur_x])
    print(bfs())
