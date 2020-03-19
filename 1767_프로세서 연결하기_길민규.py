import sys
sys.stdin = open('input.txt','r')

from copy import deepcopy

def connected(connect,dir,y,x):
    connect = deepcopy(connect)
    # 연결이 완료된 1은 4로 변경
    for go in dir:
        # 위쪽으로 전선 연결
        if go == 0:
            connect[y][x] = 4
            for dy in range(y-1,-1,-1):
                if connect[dy][x] == 2 or connect[dy][x] == 1:
                    while dy != y - 1:
                        dy += 1
                        connect[dy][x] = 0
                    connect[y][x] = 1
                    break
                connect[dy][x] = 2
        # 오른쪽으로 전선 연결
        elif go == 1:
            connect[y][x] = 4
            for dx in range(x+1,N):
                if connect[y][dx] == 2 or connect[y][dx] == 1:
                    while dx != x + 1:
                        dx -= 1
                        connect[y][dx] = 0
                    connect[y][x] = 1
                    break
                connect[y][dx] = 2
        # 아래로 전선 연결
        elif go == 2:
            connect[y][x] = 4
            for dy in range(y+1,N):
                if connect[dy][x] == 2 or connect[dy][x] == 1:
                    while dy != y + 1:
                        dy -= 1
                        connect[dy][x] = 0
                    connect[y][x] = 1
                    break
                connect[dy][x] = 2
        # 왼쪽으로 전선 연결
        elif go == 3:
            connect[y][x] = 4
            for dx in range(x-1,-1,-1):
                if connect[y][dx] == 2 or connect[y][dx] == 1:
                    while dx != x - 1:
                        dx += 1
                        connect[y][dx] = 0
                    connect[y][x] = 1
                    break
                connect[y][dx] = 2
    return connect

def check(connect, line, idx):
    # 현재까지 변경된 수가 남은 line[idx] 부분을 다 확인해도 최대 연결 수를 넘지 못하면 return
    if sum(change) + len(line) - idx < result[0]:
        return

    # 모든 경우의 수를 다 읽고 나면 최솟값 출력
    if idx == len(line):
        # 최대로 연결 된 갯수 세기
        cnt = 0
        for i in range(N):
            cnt += connect[i].count(4)
        # 전선의 갯수 세기
        cnt_2 = 0
        for i in range(N):
            cnt_2 += connect[i].count(2)

        # 연결 갯수 max로 초기화하며 그때의 전선 갯수 초기화
        if cnt > result[0]:
            result[0] = cnt
            result[1] = cnt_2
        # 연결 갯수가 max값으로 똑같다면, 전선 갯수 min값으로 초기화
        elif cnt == result[0]:
            result[1] = min(result[1],cnt_2)
        return

    confirm = line[idx]
    y, x = confirm
    for i in [0,1,2,3]:
        next_connect = connected(connect,[i],y,x)
        # 연결 완료 될 때마다 change 변경
        if next_connect[y][x] == 4:
            change[idx] = 1
        check(next_connect,line,idx + 1)
        change[idx] = 0


for t in range(1,int(input())+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    connect = deepcopy(board)

    # index = 0 은 연결완료된 최대 수, index = 1은 최대 연결 완료 되었을 때의 최소 전선 수
    result = [0, N**2 + 1]

    line = []
    for i in range(1,N-1):
        for j in range(1,N-1):
            if board[i][j] == 1:
                line.append((i,j))

    change = [0] * len(line)
    check(connect,line,0)
    print('#{} {}'.format(t,result[1]))

