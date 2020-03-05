import sys
sys.stdin = open('sample_input (1).txt','r')

from copy import deepcopy

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def go(y,x,cnt):
    maxv[0] = max(maxv[0],cnt)
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or check[ny][nx] >= check[y][x]:
            continue
        if check[ny][nx] < check[y][x]:
            go(ny,nx,cnt+1)

tc = int(input())
for t in range(1,tc+1):
    N, K = map(int,input().split())
    road = [list(map(int,input().split())) for _ in range(N)]
    check = deepcopy(road)
    mh = 0
    for i in range(N):
        mh = max(mh,max(road[i]))

    maxv = [0]

    for y in range(N):
        for x in range(N):
            if road[y][x] == mh:
                # 한 칸씩 K(1~5)만큼 순서대로 뺀다
                cut = 1
                while cut != K + 1:
                    for i in range(N):
                        for j in range(N):
                            check[i][j] -= cut
                            if check[i][j] < 0:
                                check[i][j] = 0
                            go(y,x,1)
                            check = deepcopy(road)
                    cut += 1

    print('#{} {}'.format(t,maxv[0]))
