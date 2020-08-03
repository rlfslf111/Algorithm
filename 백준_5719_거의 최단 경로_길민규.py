import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappush, heappop

def djikstra(x,go):
    q = deque()
    temp = []
    ans = [1231231]*N
    maxv = 1231231
    heappush(temp, [0,x,str(S)+' '])
    ans[x] = 0
    while temp:
        w, x, dir = heappop(temp)
        if x == D and go == 1:
            if w < maxv:
                maxv = w
                q = deque()
                q.append(dir)
            elif w == maxv:
                q.append(dir)

        for ny, nx in road[x]:
            if visit[x][nx] == 0:
                continue
            ny += w
            if ny <= ans[nx]:
                ans[nx] = ny
                heappush(temp, [ny,nx,dir+str(nx)+' '])

    if go == 1:
        while q:
            dir = q.pop()
            dir = dir.split()
            for i in range(len(dir)):
                xgo = int(dir[i])
                if i == 0:
                    xfrom = xgo
                    continue
                visit[xfrom][xgo] = 0
                xfrom = xgo
    else:
        if ans[D] == 1231231:
            print(-1)
        else:
            print(ans[D])

while 1:
    N, M = map(int,input().split())
    if (N == 0) or (M == 0):
        break
    S, D = map(int,input().split())

    road = [[] for _ in range(N)]
    visit = [[0]*N  for _ in range(N)]
    for i in range(M):
        U, V, P = map(int,input().split())
        road[U].append((P,V))
        visit[U][V] = P

    djikstra(S,1)
    djikstra(S,2)