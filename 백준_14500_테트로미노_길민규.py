import sys

dy, dx = [-1,0,1,0], [0,1,0,-1]

def dfs(y,x,k,sum):
    if k == 4:
        maxv[0] = max(maxv[0],sum)
        return
    else:
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < y and nx < x:
                continue
            if ny < 0 or ny >= N or nx < 0 or nx >= M or visit[ny][nx] == 1:
                continue
            if visit[ny][nx] == 0:
                visit[ny][nx] = 1
                dfs(ny,nx,k+1,sum+board[ny][nx])
                visit[ny][nx] = 0

def perm(k):
    if k == 3:
        ans = combi[:]
        com.append(ans)
    else:
        for i in range(len(n)):
            if not cp[i]:
                cp[i] = True
                combi.append(n[i])
                perm(k+1)
                combi.pop()
                for j in range(i+1,len(n)):
                    cp[j] = False

N, M = map(int,sys.stdin.readline().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
maxv = [0]

combi = []
n = list(range(4))
cp = [False] * 4
com = []
perm(0)

for y in range(N):
    for x in range(M):
        visit[y][x] = 1
        dfs(y,x,1,board[y][x])
        visit[y][x] = 0

        # ㅗ, ㅏ, ㅜ, ㅓ 모양 탐색하기
        for i in range(len(com)):
            sum1 = board[y][x]
            for j in range(len(com[i])):
                ni, nj = y + dy[com[i][j]], x + dx[com[i][j]]
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                sum1 += board[ni][nj]
            maxv[0] = max(maxv[0],sum1)

print(maxv[0])