dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(y,x,cnt):
    if maxv[0] < cnt:
        maxv[0] = cnt
        ans.append(maxv[0])
    if 26 in ans:
        return
    for i in range(len(dy)):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            continue
        num = to_num(ny,nx)
        if visit[num] == 1:
            continue
        visit[num] = 1
        dfs(ny,nx,cnt+1)
        visit[num] = 0

def to_num(y,x):
    return ord(board[y][x]) - ord('A')

R, C = map(int,input().split())
board = [list(input()) for _ in range(R)]
visit = [0] * 26
visit[to_num(0,0)] = 1
maxv = [0]
ans = []
dfs(0,0,1)
print(maxv[0])