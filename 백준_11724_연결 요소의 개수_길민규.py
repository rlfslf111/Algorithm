from collections import deque
def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 1
    while q:
        v = q.popleft()
        for e in check[v]:
            if not visit[e]:
                visit[e] = 1
                q.append(e)

N, M = map(int,input().split())
check = [[] for _ in range(N+1)]
visit = [0] * (N+1)
for m in range(M):
    A, B = map(int,input().split())
    check[A].append(B)
    check[B].append(A)

cnt = 0
for i in range(1,N+1):
    if visit[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)