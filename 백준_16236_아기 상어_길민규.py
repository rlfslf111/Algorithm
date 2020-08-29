import sys
input = sys.stdin.readline

from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def find_time():
    visit = [[0] * N for _ in range(N)]
    check = [[0] * N for _ in range(N)]
    q = deque()
    q.append((baby_y[0],baby_x[0]))
    visit[baby_y[0]][baby_x[0]] = 1
    minv = 0
    while q:
        y, x = q.popleft()
        # 잡아 먹을 물고기를 찾으러 출발
        for k in range(len(dy)):
            ny, nx = y + dy[k], x + dx[k]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            elif visit[ny][nx] == 0 and sea[ny][nx] <= baby_size[0]:
                visit[ny][nx] = visit[y][x] + 1
                q.append((ny,nx))

        # 잡아 먹을 물고기를 발견했다면,
        if check[y][x] == 0 and sea[y][x] != 0 and sea[y][x] < baby_size[0]:
            # 처음 발견한 물고기라면,
            if minv == 0:
                minv = visit[y][x]
                check[y][x] = minv
            # 처음으로 발견한 물고기가 아니라면,
            elif visit[y][x] == minv:
                check[y][x] = minv

    # 모든 맵을 다 확인 했다면,
    for i in range(N):
        for j in range(N):
            if check[i][j] != 0:
                # 물고기를 먹은 자리로 아기 상어 위치 초기화
                baby_y[0] = i
                baby_x[0] = j
                sea[i][j] = 0
                return check[i][j] - 1

    # 먹을 물고기가 없으면,
    return 0


N = int(input())
sea = []
baby_y = []
baby_x = []
baby_size = [2]
for i in range(N):
    sea.append(list(map(int,input().split())))
    for j in range(N):
        if sea[i][j] == 9:
            # 아기 상어 처음 위치 설정
            baby_y.append(i)
            baby_x.append(j)
            sea[i][j] = 0

time = 1231231
ans = 0
eatcnt = 0
while time:
    time = find_time()
    ans += time
    # 먹은 물고기가 있으면,
    if time != 0:
        eatcnt += 1
        if eatcnt == baby_size[0]:
            baby_size[0] += 1
            eatcnt = 0
print(ans)