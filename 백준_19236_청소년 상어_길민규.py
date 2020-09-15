import sys
input = sys.stdin.readline
from copy import deepcopy

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]

# 물고기 위치 변경
def move_fish():
    for number in range(1,17):
        # 이미 먹힌 물고기는 pass
        if number not in fish_num:
            continue
        else:
            # 이미 움직인 물고기인지 아닌지 판단
            move_flag = False
            for i in range(4):
                for j in range(4):
                    if not move_flag and sea[i][j][0] == number:
                        y, x, dir = i, j, sea[i][j][1]
                        while 1:
                            ny, nx = y + dy[dir], x + dx[dir]
                            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4 or sea[ny][nx][0] == -1:
                                dir += 1
                                if dir > 7:
                                    dir = 0
                            else:
                                fish_info = sea[ny][nx]
                                sea[ny][nx] = [sea[y][x][0], dir]
                                sea[y][x] = fish_info
                                move_flag = True
                                break


def move_shark(y,x,dir,sum):
    # 복사본 떠놓기 (sea를 원래대로 돌려놓을 때 필요)
    copy_sea = deepcopy(sea)
    # 물고기 움직임으로 dfs 시작
    move_fish()

    if ans[0] < sum:
        ans[0] = sum

    # sea 가 4x4 이므로 최대 3칸 움직일 수 있다.
    for i in range(1,4):
        ny = y + (dy[dir] * i)
        nx = x + (dx[dir] * i)

        # 범위를 벗어나면 집으로 간다.
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            break

        # 물고기가 없으면 continue
        if sea[ny][nx][0] == 0:
            continue

        num, fish_dir = sea[ny][nx]
        sea[y][x][0] = 0
        sea[ny][nx][0] = -1
        fish_num.remove(num)
        move_shark(ny, nx, fish_dir, sum + num)
        sea[y][x][0] = -1
        sea[ny][nx][0] = num
        fish_num.append(num)

    # return 전에 원래의 모습으로 돌려놓기
    for i in range(4):
        for j in range(4):
            sea[i][j] = copy_sea[i][j]


sea = [[] for _ in range(4)]
# 물고기 numbering
fish_num = [i for i in range(1,17)]
for i in range(4):
    temp = list(map(int,input().split()))
    for j in range(0,len(temp) - 1,2):
        sea[i].append([temp[j],temp[j+1] - 1])

# 상어가 처음으로 들어간다.
fish_num.remove(sea[0][0][0])
first_eat = sea[0][0][0]
# 상어는 -1, 공백은 0
sea[0][0][0] = -1

ans = [0]
# 상어가 물고기를 찾아간다.
move_shark(0, 0, sea[0][0][1], first_eat)
print(ans[0])

