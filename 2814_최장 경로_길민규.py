def dfs(v,cnt):
    visited[v] = 1
    for i in check[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i,cnt+1)
            visited[i] = 0
    maxv[0] = max(maxv[0],cnt)

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    check = [[] for _ in range(N+1)]
    for m in range(M):
        X, Y = map(int,input().split())
        check[X].append(Y)
        check[Y].append(X)

    visited = [0] * (N+1)
    maxv = [0]
    for i in range(1,N+1):
        dfs(i,1)
        visited = [0] * (N + 1)

    print('#{} {}'.format(t,maxv[0]))
