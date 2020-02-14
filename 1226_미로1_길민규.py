import sys
sys.stdin = open('maze.txt','r')

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def dfs(y,x):
    global ans
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= 16 or ny < 0 or ny >= 16 or maze[ny][nx] == 1:
            continue
        if maze[ny][nx] == 3:
            ans = 1
            return
        if maze[ny][nx] == 0:
            maze[ny][nx] = 1
            dfs(ny,nx)

for t in range(10):
    T = int(input())
    maze = [list(input()) for _ in range(16)]
    # maze를 int로 변환
    for i in range(16):
        maze[i] = [int(_) for _ in maze[i]]

    for i in range(16):
        # idx == 2에서 2를 찾으면 시작
        if maze[1][i] == 2:
            sp = i
            break
    ans = 0

    dfs(1,sp)
    print('#{} {}'.format(T,ans))

