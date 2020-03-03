from copy import deepcopy

# dir 0,1,2,3 == 상 우 하 좌
def check_office(office, dir, y, x):
    office = deepcopy(office)
    for looking in dir:
        # 위를 볼 때
        if looking == 0:
            for dy in range(y,-1,-1):
                if office[dy][x] == 6:
                    break
                elif office[dy][x] != 0:
                    continue
                else:
                    office[dy][x] = 7
        # 오른쪽을 볼 때
        elif looking == 1:
            for dx in range(x,M):
                if office[y][dx] == 6:
                    break
                elif office[y][dx] != 0:
                    continue
                else:
                    office[y][dx] = 7
        # 아래를 볼 때
        elif looking == 2:
            for dy in range(y,N):
                if office[dy][x] == 6:
                    break
                elif office[dy][x] != 0:
                    continue
                else:
                    office[dy][x] = 7
        # 왼쪽을 볼 때
        elif looking == 3:
            for dx in range(x,-1,-1):
                if office[y][dx] == 6:
                    break
                elif office[y][dx] != 0:
                    continue
                else:
                    office[y][dx] = 7
    return office

def monitor(office,cctv,idx):
    if idx == len(cctv):
        cnt = 0
        for i in range(N):
            cnt += office[i].count(0)
        min_value[0] = min(min_value[0],cnt)
        return

    cctv_see = cctv[idx]
    y, x, camera = cctv_see
    if camera == 1:
        for i in [0,1,2,3]:
            next_office = check_office(office, [i], y, x)
            monitor(next_office, cctv, idx + 1)
    elif camera == 2:
        for i in [[0,2],[1,3]]:
            next_office = check_office(office, i, y, x)
            monitor(next_office, cctv, idx + 1)
    elif camera == 3:
        for i in [[0,1],[1,2],[2,3],[3,0]]:
            next_office = check_office(office, i, y, x)
            monitor(next_office, cctv, idx + 1)
    elif camera == 4:
        for i in [[0,1,2],[1,2,3],[2,3,0],[3,0,1]]:
            next_office = check_office(office, i, y, x)
            monitor(next_office, cctv, idx + 1)
    elif camera == 5:
        next_office = check_office(office, [0,1,2,3], y, x)
        monitor(next_office, cctv, idx + 1)


N, M = map(int,input().split())
input_ = [list(map(int,input().split())) for _ in range(N)]
office = deepcopy(input_)

cctv = []
for y in range(N):
    for x in range(M):
        if 1 <= input_[y][x] <= 5:
            cctv.append([y,x,input_[y][x]])

min_value = [N*M+1]
monitor(office,cctv,0)
print(min_value[0])