dy = [-1,0,1,0]
dx = [0,1,0,-1]
def dfs(y,x,step):
    if step == int(X):
        per = 1
        for i in range(len(ans)):
            if ans[i][0] == -1 and ans[i][1] == 0:
                per *= N
            elif ans[i][0] == 0 and ans[i][1] == 1:
                per *= E
            elif ans[i][0] == 1 and ans[i][1] == 0:
                per *= S
            elif ans[i][0] ==0 and ans[i][1] == -1:
                per *= W
        result.append(per)
        return
    else:
        visit[y][x] = 1
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if visit[ny][nx] != 1:
                ans.append([dy[i],dx[i]])
                visit[ny][nx] = 1
                dfs(ny,nx,step+1)
                visit[ny][nx] = 0
                ans.pop()

X, E, W, S, N = map(float,input().split())
E, W, S, N = E/100, W/100, S/100, N/100
visit = [[0]*50 for _ in range(50)]
ans = []
result = []
dfs(25,25,0)
print(sum(result))
