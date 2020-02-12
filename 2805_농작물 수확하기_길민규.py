import sys
sys.stdin = open('farm.txt','r')

tc = int(input())
for t in range(tc):
    N = int(input())
    farm = [input() for _ in range(N)]
    board = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            board[y][x] = int(farm[y][x])
    #윗부분 다이아몬드
    idx = 0
    manuplate = []
    for y in range(N//2+1):
        for x in range(N):
            pass
        manuplate.append(board[y][N//2-idx:N//2+idx+1])
        idx+=1
        if idx == N//2:
            break
    #아랫부분 다이아몬드
    idx2 = N//2
    for y in range(N//2+1):
        for x in range(N):
            pass
        manuplate.append(board[y+N//2][N//2-idx2:N//2+idx2+1])
        idx2-=1

    sum = 0
    for y in range(N):
        for x in range(len(manuplate[y])):
            sum+=manuplate[y][x]
    print('#{} {}'.format(t+1,sum))

