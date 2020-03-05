def check():
    cnt = 0

    # 가로 확인
    for y in range(5):
        zero_cnt = 1
        if cheolsu[y][0] == 0:
            nx = 0
            while 1:
                nx += 1
                if nx >= 5 or cheolsu[y][nx] != 0:
                    break
                zero_cnt += 1
        if zero_cnt == 5:
            cnt += 1

    # 세로 확인
    for x in range(5):
        zero_cnt1 = 1
        if cheolsu[0][x] == 0:
            ny = 0
            while 1:
                ny += 1
                if ny >= 5 or cheolsu[ny][x] != 0:
                    break
                zero_cnt1 += 1
        if zero_cnt1 == 5:
            cnt += 1

    # 대각 확인
    if cheolsu[0][0] == 0:
        zero_cnt2 = 1
        ny = 0
        nx = 0
        while 1:
            ny += 1
            nx += 1
            if ny >= 5 or nx >= 5 or cheolsu[ny][nx] != 0:
                break
            zero_cnt2 += 1
        if zero_cnt2 == 5:
            cnt += 1

    # 역 대각 확인
    if cheolsu[4][0] == 0:
        zero_cnt3 = 1
        ny = 4
        nx = 0
        while 1:
            ny += (-1)
            nx += 1
            if ny < 0 or nx >= 5 or cheolsu[ny][nx] != 0:
                break
            zero_cnt3 += 1
        if zero_cnt3 == 5:
            cnt += 1

    if cnt >= 3:
        return True
    return False

cheolsu = [list(map(int,input().split())) for _ in range(5)]
mc = [list(map(int,input().split())) for _ in range(5)]
mc_su = []
for y in range(5):
    for x in range(5):
        mc_su.append(mc[y][x])

speak = 0
while speak != len(mc_su):
    if check():
        break
    for y in range(5):
        for x in range(5):
            if cheolsu[y][x] == mc_su[speak]:
                cheolsu[y][x] = 0
                break

    speak += 1

print(speak)