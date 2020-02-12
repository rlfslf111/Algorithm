import sys
sys.stdin = open('magnetic.txt','r')

dy = [-1,1]

for t in range(10):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                ny = y
                while True:
                    ny += dy[1]
                    if ny < 0 or ny >= N:
                        break
                    if board[ny][x] == 2:
                        board[y][x] = 0
                        board[ny-1][x] = 1
                        break
                    board[y][x] = 0
    for x in range(N):
        if board[N-1][x] == 1:
            board[N-1][x] = 0

    for y in range(N-1,-1,-1):
        for x in range(N):
            if board[y][x] == 2:
                ny = y
                while True:
                    ny += dy[0]
                    if ny < 0 or ny >= N:
                        break
                    if board[ny][x]==1:
                        break
                    board[y][x] = 0

    count = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                count+=1
    print('#{} {}'.format(t+1,count))