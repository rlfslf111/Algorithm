dy = [1,0]
dx = [0,1]

def dfs(y,x,sum):
    if y == N - 1 and x == N - 1:
        if sum < minv[0]:
            minv[0] = sum
        return
    if sum >= minv[0]:
        return

    for i in range(len(dy)):
        ny, nx = y + dy[i], x + dx[i]
        if ny >= N or nx >= N:
            continue
        dfs(ny,nx,sum+board[ny][nx])

for t in range(1,int(input())+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    minv = [1231231]
    dfs(0,0,board[0][0])
    print('#{} {}'.format(t,minv[0]))