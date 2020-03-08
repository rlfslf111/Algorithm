# 0 = N 극, 1 = S 극
gear1 = list(map(int,list(input())))
gear2 = list(map(int,list(input())))
gear3 = list(map(int,list(input())))
gear4 = list(map(int,list(input())))

step = int(input())
order = []
for i in range(step):
    num, dir = map(int,input().split())
    order.append([num,dir])

time = 0
while time != step:
    # 1번 톱니바퀴 일 때
    if order[time][0] == 1:
        dump1 = []
        # 시계방향으로 회전
        if order[time][1] == 1:
            # 2번 톱니바퀴랑 반시계 회전 확인
            rota2 = []
            if gear1[2] != gear2[6]:
                # 2번과 3번 회전 확인
                rota3 = []
                if gear2[2] != gear3[6]:
                    # 3번과 4번 회전 확인
                    rota4 = []
                    if gear3[2] != gear4[6]:
                        rota4.append(gear4[0])
                        del gear4[0]
                        gear4.insert(7,rota4[0])
                        del rota4[0]
                    rota3.append(gear3[-1])
                    del gear3[-1]
                    gear3.insert(0,rota3[0])
                    del rota3[0]
                rota2.append(gear2[0])
                del gear2[0]
                gear2.insert(7, rota2[0])
                del rota2[0]
            dump1.append(gear1[-1])
            del gear1[-1]
            gear1.insert(0, dump1[0])
            del dump1[0]
        # 반시계 방향으로 회전
        elif order[time][1] == -1:
            # 2번 톱니바퀴랑 시계 회전 확인
            rota2 = []
            if gear1[2] != gear2[6]:
                # 2번과 3번 회전 확인
                rota3 = []
                if gear2[2] != gear3[6]:
                    # 3번과 4번 회전 확인
                    rota4 = []
                    if gear3[2] != gear4[6]:
                        rota4.append(gear4[-1])
                        del gear4[-1]
                        gear4.insert(0, rota4[0])
                        del rota4[0]
                    rota3.append(gear3[0])
                    del gear3[0]
                    gear3.insert(7, rota3[0])
                    del rota3[0]
                rota2.append(gear2[-1])
                del gear2[-1]
                gear2.insert(0, rota2[0])
                del rota2[0]
            dump1.append(gear1[0])
            del gear1[0]
            gear1.insert(7, dump1[0])
            del dump1[0]

    # 2번 톱니바퀴 일 때
    elif order[time][0] == 2:
        dump2 = []
        # 시계방향으로 회전
        if order[time][1] == 1:
            # 1번 톱니바퀴랑 반시계 회전 확인
            rota1 = []
            if gear2[6] != gear1[2]:
                rota1.append(gear1[0])
                del gear1[0]
                gear1.insert(7, rota1[0])
                del rota1[0]
            # 3번 톱니바퀴 반시계 회전 확인
            rota3 = []
            if gear2[2] != gear3[6]:
                # 3번과 4번 비교
                rota4 = []
                if gear3[2] != gear4[6]:
                    rota4.append(gear4[-1])
                    del gear4[-1]
                    gear4.insert(0,rota4[0])
                    del rota4[0]
                rota3.append(gear3[0])
                del gear3[0]
                gear3.insert(7, rota3[0])
                del rota3[0]
            dump2.append(gear2[-1])
            del gear2[-1]
            gear2.insert(0, dump2[0])
            del dump2[0]
        # 반시계 방향으로 회전
        elif order[time][1] == -1:
            # 1번 톱니바퀴랑 시계 회전 확인
            rota1 = []
            if gear2[6] != gear1[2]:
                rota1.append(gear1[-1])
                del gear1[-1]
                gear1.insert(0, rota1[0])
                del rota1[0]
            # 3번 톱니바퀴랑 시계 회전 확인
            rota3 = []
            if gear2[2] != gear3[6]:
                # 4번 반시계 확인
                rota4 = []
                if gear3[2] != gear4[6]:
                    rota4.append(gear4[0])
                    del gear4[0]
                    gear4.insert(7,rota4[0])
                    del rota4[0]
                rota3.append(gear3[-1])
                del gear3[-1]
                gear3.insert(0, rota3[0])
                del rota3[0]
            dump2.append(gear2[0])
            del gear2[0]
            gear2.insert(7, dump2[0])
            del dump2[0]

    # 3번 톱니바퀴 일 때
    elif order[time][0] == 3:
        dump3 = []
        # 시계방향으로 회전
        if order[time][1] == 1:
            # 2번 톱니바퀴랑 반시계 회전 확인
            rota2 = []
            if gear3[6] != gear2[2]:
                # 1번 톱니바퀴 시계 확인
                rota1 = []
                if gear2[6] != gear1[2]:
                    rota1.append(gear1[-1])
                    del gear1[-1]
                    gear1.insert(0,rota1[0])
                    del rota1[0]
                rota2.append(gear2[0])
                del gear2[0]
                gear2.insert(7,rota2[0])
                del rota2[0]
            # 4번 톱니바퀴 반시계 회전 확인
            rota4 = []
            if gear3[2] != gear4[6]:
                rota4.append(gear4[0])
                del gear4[0]
                gear4.insert(7,rota4[0])
                del rota4[0]
            dump3.append(gear3[-1])
            del gear3[-1]
            gear3.insert(0,dump3[0])
            del dump3[0]
        # 반시계 방향으로 회전
        elif order[time][1] == -1:
            # 2번 톱니바퀴랑 시계 회전 확인
            rota2 = []
            if gear3[6] != gear2[2]:
                # 1번 반시계 확인
                rota1 = []
                if gear2[6] != gear1[2]:
                    rota1.append(gear1[0])
                    del gear1[0]
                    gear1.insert(7,rota1[0])
                    del rota1[0]
                rota2.append(gear2[-1])
                del gear2[-1]
                gear2.insert(0,rota2[0])
                del rota2[0]
            # 4번 톱니바퀴랑 시계 회전 확인
            rota4 = []
            if gear3[2] != gear4[6]:
                rota4.append(gear4[-1])
                del gear4[-1]
                gear4.insert(0,rota4[0])
                del rota4[0]
            dump3.append(gear3[0])
            del gear3[0]
            gear3.insert(7,dump3[0])
            del dump3[0]

    # 4번 톱니바퀴일 때
    elif order[time][0] == 4:
        dump4 = []
        # 시계방향으로 회전
        if order[time][1] == 1:
            # 3번 톱니바퀴랑 반시계 회전 확인
            rota3 = []
            if gear4[6] != gear3[2]:
                # 3번과 2번 회전 확인
                rota2 = []
                if gear3[6] != gear2[2]:
                    # 2번과 1번 회전 확인
                    rota1 = []
                    if gear2[6] != gear1[2]:
                        rota1.append(gear1[0])
                        del gear1[0]
                        gear1.insert(7, rota1[0])
                        del rota1[0]
                    rota2.append(gear2[-1])
                    del gear2[-1]
                    gear2.insert(0, rota2[0])
                    del rota2[0]
                rota3.append(gear3[0])
                del gear3[0]
                gear3.insert(7, rota3[0])
                del rota3[0]
            dump4.append(gear4[-1])
            del gear4[-1]
            gear4.insert(0, dump4[0])
            del dump4[0]

        # 반시계 방향으로 회전
        elif order[time][1] == -1:
            # 3번 톱니바퀴랑 시계 회전 확인
            rota3 = []
            if gear4[6] != gear3[2]:
                # 3번과 2번 회전 확인
                rota2 = []
                if gear3[6] != gear2[2]:
                    # 2번과 1번 회전 확인
                    rota1 = []
                    if gear2[6] != gear1[2]:
                        rota1.append(gear1[-1])
                        del gear1[-1]
                        gear1.insert(0, rota1[0])
                        del rota1[0]
                    rota2.append(gear2[0])
                    del gear2[0]
                    gear2.insert(7, rota2[0])
                    del rota2[0]
                rota3.append(gear3[-1])
                del gear3[-1]
                gear3.insert(0, rota3[0])
                del rota3[0]
            dump4.append(gear4[0])
            del gear4[0]
            gear4.insert(7, dump4[0])
            del dump4[0]

    time += 1

ans = gear1[0] + (gear2[0]*2) + (gear3[0]*4) + (gear4[0]*8)
print(ans)