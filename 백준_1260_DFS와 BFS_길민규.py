from collections import deque

def dfs(visit,v):
    for i in check[v]:
        if i not in visit:
            visit.append(i)
            dfs(visit,i)
    return visit

def bfs(v):
    visit = [0] * (N+1)
    q = deque()
    q.append(v)
    visit[v] = 1
    while q:
        v = q.popleft()
        ans.append(v)
        for e in check[v]:
            if not visit[e]:
                visit[e] = 1
                q.append(e)


N, M, V = map(int,input().split())
check = [[] for _ in range(N+1)]
ans = []
for m in range(M):
    A, B = map(int,input().split())
    check[A].append(B)
    check[B].append(A)

for i in range(1,len(check)):
    check[i].sort()

print(*dfs([V],V))
bfs(V)
print(*ans)