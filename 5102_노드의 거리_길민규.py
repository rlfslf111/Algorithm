from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visit = [0]*(V+1)
    visit[s] = 1
    cnt = 0
    while q:
        for i in range(len(q)):
            s = q.popleft()
            if s == G:
                return cnt
            for k in check[s]:
                if not visit[k]:
                    visit[k] = 1
                    q.append(k)
        cnt += 1
    return 0

for t in range(1,int(input())+1):
    V, E = map(int,input().split())

    check = [[] for _ in range(V+1)]
    for e in range(E):
        A, B = map(int,input().split())
        check[A].append(B)
        check[B].append(A)

    S, G = map(int,input().split())

    print('#{} {}'.format(t,bfs(S)))