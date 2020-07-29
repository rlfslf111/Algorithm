import sys
input = sys.stdin.readline

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visit = [1] + [0 for _ in range(N)]
    visit[start] = 1
    cnt = 0
    while q:
        fly = q.popleft()
        for e in check[fly]:
            if not visit[e]:
                visit[e] = 1
                cnt += 1
                q.append(e)
    return cnt

for t in range(int(input())):
    N, M = map(int,input().split())

    check = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int,input().split())
        check[a].append(b)
        check[b].append(a)

    print(bfs(1))
