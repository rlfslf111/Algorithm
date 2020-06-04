from collections import deque

def friends(sang):
    q = deque()
    q.append(sang)
    visit[sang] = 1
    invite = 0
    cnt = 0
    while q:
        if cnt >= 2:
            break
        for _ in range(len(q)):
            v = q.popleft()
            for e in check[v]:
                if not visit[e]:
                    visit[e] = 1
                    invite += 1
                    q.append(e)
        cnt += 1
    return invite

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    check = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int,input().split())
        check[a].append(b)
        check[b].append(a)
    visit = [0 for _ in range(N+1)]

    print('#{} {}'.format(t,friends(1)))