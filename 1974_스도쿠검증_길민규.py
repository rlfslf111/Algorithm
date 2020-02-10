
import sys
sys.stdin = open('sdoqu.txt','r')

def verify(sdoqu):
    #가로 확인
    for y in range(len(sdoqu)):
        for x in range(len(sdoqu)-1):
            for z in range(x+1,len(sdoqu)):
                if sdoqu[y][x] == sdoqu[y][z]:
                    return 0

    #세로 확인
    for x in range(len(sdoqu)):
        for y in range(len(sdoqu)-1):
            for z in range(y+1,len(sdoqu)):
                if sdoqu[y][x] == sdoqu[z][x]:
                    return 0

    #대각 확인
    dy = [0,0,0,1,1,1,2,2,2]
    dx = [0,1,2,0,1,2,0,1,2]
    three_list = []
    for y in range(0,len(sdoqu),3):
        for x in range(0,len(sdoqu),3):
            sum = 0
            for k in range(len(dy)):
                ny = y + dy[k]
                nx = x + dx[k]
                sum += sdoqu[ny][nx]
            else:
                three_list.append(sum)
    #1~9까지의 합은 45다 델타를 이용해 하나씩 꺼낸다음 합이 45가 아니면 return 0을 시켜라
    for very in three_list:
        if very != 45:
            return 0
    return 1

tc = int(input())
for t in range(tc):
    sdoqu = [list(map(int,input().split())) for _ in range(9)]
    print('#{} {}'.format(t+1,verify(sdoqu)))