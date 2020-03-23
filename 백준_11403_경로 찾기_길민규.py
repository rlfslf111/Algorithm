from collections import deque

def bfs(k):
    while q:
        i, j = q.popleft()
        check[i][j] = 1
        for e in range(N):
            if graph[j][e] == 1 and check[k][e] == 0:
                check[k][e] = 1
                q.append((j, e))

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            q.append((i,j))
            bfs(i)

for i in range(N):
    print(*check[i])