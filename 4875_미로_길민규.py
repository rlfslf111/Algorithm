import sys
sys.stdin = open('maze.txt','r')

dy = [0,0,1,-1]
dx = [1,-1,0,0]
def find(y,x):
    global ans
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or maze[ny][nx] == 1:
            continue
        if maze[ny][nx] == 3:
            ans = 1
            return
        if maze[ny][nx] == 0:
            maze[ny][nx] = 7
            find(ny,nx)

tc = int(input())
for t in range(tc):
    N = int(input())
    maze = [list(map(int,list(input()))) for _ in range(N)]

    ans = 0
    y = 0
    x = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                y = i
                x = j
                break
    find(y,x)
    print('#{} {}'.format(t+1,ans))
