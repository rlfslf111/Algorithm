import sys
from itertools import combinations
from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(spread):
    # deepcopy를 사용할 경우 시간 초과가 발생할 가능성이 있음.
    check = [[0]*N for _ in range(N)]
    q = deque()
    for i in spread:
        iy, ix = i
        check[iy][ix] = -1
        q.append((iy,ix,1))

    infection = 0
    max_value = 0

    while q:
        y, x, time = q.popleft()

        if time > minv:
            break

        # 감염시킨 갯수가 처음 0의 갯수와 같다면,
        if infection == z_cnt[0]:
            return max_value

        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] == 1:
                continue

            # 비활성 바이러스를 만난다면, 활성화만
            elif check[ny][nx] == 0 and board[ny][nx] == 2:
                check[ny][nx] = time
                q.append((ny,nx,time+1))

            # 바이러스가 없는 빈 칸을 만났을 경우
            elif check[ny][nx] == 0:
                check[ny][nx] = time
                q.append((ny,nx,time+1))
                infection += 1
                max_value = max(time,max_value)

    return -1

N, M = map(int,sys.stdin.readline().split())
virus = []
board = []
# 초기 빈칸(0)의 갯수를 세어놓는다.
z_cnt = [0]
for y in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
    for x in range(N):
        if board[y][x] == 2:
            virus.append((y,x))
        elif board[y][x] == 0:
            z_cnt[0] += 1

flag = False
minv = N**2 + 1

for i in combinations(virus,M):
    ans = bfs(i)
    if ans != -1:
        flag = True
        minv = min(minv,ans)

if flag:
    print(minv)
else:
    print(-1)
