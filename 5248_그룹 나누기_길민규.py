from collections import deque

def bfs(k):
    q = deque()
    q.append(k)
    visit[k] = 1
    while q:
        a = q.popleft()
        for i in check[a]:
            if not visit[i]:
                visit[i] = 1
                q.append(i)

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    num = [0] + [1 for _ in range(N)]
    check = [[] for _ in range(N+1)]
    visit = [0] * (N+1)

    ls = list(map(int,input().split()))
    for i in range(0,len(ls),2):
        check[ls[i]].append(ls[i+1])
        check[ls[i+1]].append(ls[i])

    ans = 0
    for k in range(1,N+1):
        if not visit[k]:
            bfs(k)
            ans += 1
    print('#{} {}'.format(t,ans))