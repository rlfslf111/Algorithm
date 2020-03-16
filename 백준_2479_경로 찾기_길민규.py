from collections import deque

def bfs(v):
    flag = False
    q = deque()
    q.append(v)
    visit = [0] * (N+1)
    visit[v] = 1
    ans = [[] for _ in range(N+1)]
    ans[v].append(v)
    while q:
        v = q.popleft()
        if v == B:
            flag = True
            break
        for i in range(1,len(check)):
            cnt = 0
            for k in range(K):
                if check[v][k] != check[i][k] and not visit[i]:
                    cnt += 1
            if cnt == 1:
                q.append(i)
                visit[i] = 1
                ans[i] = ans[v] + [i]
    if flag:
        return ans[B]
    else:
        return [-1]

N, K = map(int,input().split())
check = [[]]
for n in range(N):
    b = list(map(int,list(input())))
    check.append(b)

A, B = map(int,input().split())

print(*bfs(A))
