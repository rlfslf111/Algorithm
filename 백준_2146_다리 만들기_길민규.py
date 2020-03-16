from collections import deque
from copy import deepcopy

dy = [-1,0,1,0]
dx = [0,1,0,-1]
# 각 대륙 별로 번호 매기기
def numbering(y,x):
    global country
    visit[y][x] = country
    v = deque()
    v.append((y,x))
    while v:
        y, x = v.popleft()
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N or visit[ny][nx] != 0:
                continue
            if world[ny][nx] == 1 and visit[ny][nx] == 0:
                visit[ny][nx] = country
                v.append((ny,nx))


# 대륙 가장자리에서 다음 대륙으로의 길이 찾기
def bfs(y,x,c_num):
    minv1 = 1231231
    q = deque()
    d = 1
    q.append((y,x,d))
    while q:
        y, x, d = q.popleft()
        for i in range(len(dy)):
            ny, nx  = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if minv1 < d:
                break
            if check[ny][nx] == 0:
                q.append((ny,nx,d+1))
                check[ny][nx] = c_num
            if check[ny][nx] != c_num:
                minv1 = min(minv1,d)
    return minv1


N = int(input())
world = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

country = 1
for y in range(N):
    for x in range(N):
        if world[y][x] == 1 and visit[y][x] == 0:
            numbering(y,x)
            country += 1

# visit 배열과 같은 copy 배열을 만들어 놓는다. (거리 check 용)
check = deepcopy(visit)

c_num = 0
result = 1231231
for y in range(N):
    for x in range(N):
        # 숫자(대륙) 바로 옆 0(바다) 에서 찾는다
        if visit[y][x] == 0:
            for i in range(len(dy)):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= N or nx < 0 or nx >= N or visit[ny][nx] == 0:
                    continue
                if visit[ny][nx] != 0:
                    c_num = visit[ny][nx]
            if c_num != 0:
                distance = bfs(y,x,c_num)
                result = min(distance,result)
                check = deepcopy(visit)
            c_num = 0

print(result)