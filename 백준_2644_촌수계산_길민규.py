from collections import deque

def bfs(v):
    flag = False
    q = deque()
    q.append(v)
    visit = [0] * (n+1)
    visit[v] = 1
    cnt = 0
    while q:
        if sec in q:
            flag = True
            break
        cnt += 1
        for i in range(len(q)):
            v = q.popleft()
            for k in check[v]:
                if not visit[k]:
                    visit[k] = 1
                    q.append(k)
    if flag:
        return cnt
    else:
        return -1

n = int(input())
fir, sec = map(int,input().split())
m = int(input())
check = [[] for _ in range(n+1)]
for M in range(m):
    x, y = map(int,input().split())
    check[y].append(x)
    check[x].append(y)

print(bfs(fir))
