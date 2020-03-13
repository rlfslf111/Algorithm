from collections import deque
def bfs(v):
    q = deque()
    q.append(v)
    visit = [0] * (N+1)
    visit[v] = 1
    cnt = 0
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            for e in check[v]:
                if not visit[e]:
                    visit[e] = 1
                    q.append(e)
        if q:
            cnt += 1
    return cnt

N = int(input())
check = [[] for _ in range(N+1)]
while 1:
    a, b = map(int,input().split())
    if a == -1 or b == -1:
        break
    check[a].append(b)
    check[b].append(a)

minv = 1231231
ans = []
for i in range(1,N+1):
    c = bfs(i)
    if c < minv:
        minv = c
        ans = [i]
    elif c == minv:
        ans.append(i)
print(minv, len(ans))
print(*ans)