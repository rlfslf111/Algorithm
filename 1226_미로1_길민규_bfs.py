import sys
sys.stdin = open('input.txt','r')

from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs():
    while q:
        y, x = q.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= 16 or nx < 0 or nx >= 16 or maze[ny][nx] == 1:
                continue
            elif maze[ny][nx] == 3:
                return 1
            elif visit[ny][nx] == 0:
                visit[ny][nx] = 1
                q.append((ny,nx))
    return 0

for t in range(10):
    tc = int(input())
    q = deque()
    visit = [[0 for _ in range(16)] for _ in range(16)]
    maze = []
    for i in range(16):
        maze.append(list(map(int,list(input()))))
        for j in range(16):
            if maze[i][j] == 2:
                q.append((i,j))
                visit[i][j] = 1
    print('#{} {}'.format(tc,bfs()))