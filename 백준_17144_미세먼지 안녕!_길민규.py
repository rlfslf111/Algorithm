dy = [-1,0,1,0]
dx = [0,1,0,-1]
def diffuse(y,x):
    diffuse_cnt = 0
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= R or nx < 0 or nx >= C or room[ny][nx] == -1:
            continue
        if room[y][x] != -1 and room[y][x] != 0:
            dust[ny][nx] += room[y][x]//5
            diffuse_cnt += 1
    dust[y][x] += (room[y][x] - ((room[y][x]//5)*diffuse_cnt))


up_dy = [-1,0,1,0]
up_dx = [0,1,0,-1]
def clean_up(y,x):
    current_y = y + 1
    while 1:
        ny = y + up_dy[dir1[0]]
        nx = x + up_dx[dir1[0]]
        if ny < 0 or ny > current_y or nx < 0 or nx >= C:
            dir1[0] += 1
        else:
            if room[ny][nx] == -1:
                room[y][x] = 0
                break
            room[y][x] = room[ny][nx]
            y, x = ny, nx

down_dy = [1,0,-1,0]
down_dx = [0,1,0,-1]
def clean_down(y,x):
    current_y = y - 1
    while 1:
        ny = y + down_dy[dir2[0]]
        nx = x + down_dx[dir2[0]]
        if ny < current_y or ny >= R or nx < 0 or nx >= C:
            dir2[0] += 1
        else:
            if room[ny][nx] == -1:
                room[y][x] = 0
                break
            room[y][x] = room[ny][nx]
            y, x = ny, nx

R, C, T = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]
dust = [[0]*C for _ in range(R)]
dir1 = [0]
dir2 = [0]

time = 0
while time < T:
    # 미세먼지 확산
    for y in range(R):
        for x in range(C):
            if room[y][x] != 0 and room[y][x] != -1:
                diffuse(y,x)
    for y in range(R):
        for x in range(C):
            if room[y][x] != -1:
                room[y][x] = dust[y][x]
    dust = [[0] * C for _ in range(R)]

    #공기청정기로 한 칸씩 미루기
    for y in range(R):
        if room[y][0] == -1:
            clean_up(y-1,0)
            dir1[0] = 0
            break
    for y in range(R-1,-1,-1):
        if room[y][0] == -1:
            clean_down(y+1,0)
            dir2[0] = 0
            break
    time += 1

ans = 0
for y in range(R):
    for x in range(C):
        if room[y][x] != -1:
            ans += room[y][x]
print(ans)