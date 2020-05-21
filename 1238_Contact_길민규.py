from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visit = [0] * (N+1)
    visit[v] = 1
    i = 0
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            ans[i].append(v)
            for e in check[v]:
                if not visit[e]:
                    visit[e] = 1
                    q.append(e)
        i += 1

for t in range(1,11):
    N, start = map(int,input().split())
    ls = list(map(int,input().split()))

    check = [[] for _ in range(101)]

    for i in range(0,N,2):
        check[ls[i]].append(ls[i+1])


    ans = [[] for _ in range(100)]
    bfs(start)
    for k in range(len(ans)-1,-1,-1):
        if ans[k]:
            maxv = max(ans[k])
            break
    print('#{} {}'.format(t,maxv))