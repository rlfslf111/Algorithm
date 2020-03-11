import sys
sys.stdin = open('2048.txt','r')

#합치는 함수 시작
def move(dir):
    if dir == 0: # up일 경우
        for i in range(N):
            for j in range(N-1):
                if board[j][i] == 0:
                    for k in range(j+1,N):
                        if board[k][i] != 0:
                            board[j][i] = board[k][i]
                            board[k][i] = 0
                            break

    elif dir == 1: #down일 경우
        for i in range(N):
            for j in range(N-1,0,-1):
                if board[j][i] == 0:
                    for k in range(j-1,-1,-1):
                        if board[k][i] != 0:
                            board[j][i] = board[k][i]
                            board[k][i] = 0
                            break
    elif dir == 2: # left일 경우
        for i in range(N):
            for j in range(N-1):
                if board[i][j] == 0:
                    for k in range(j+1,N):
                        if board[i][k] != 0:
                            board[i][j] = board[i][k]
                            board[i][k]=0
                            break
    elif dir == 3:
        for i in range(N):
            for j in range(N-1,0,-1):
                if board[i][j] == 0:
                    for k in range(j-1,-1,-1):
                        if board[i][k] != 0:
                            board[i][j] = board[i][k]
                            board[i][k]=0
                            break

#미는 함수 시작
def plus(dir):
    if dir == 0:
        for i in range(N):
            for j in range(N-1):
                if board[j][i] != 0:
                    for k in range(j+1,N):
                        if board[k][i] != 0:
                            if board[k][i] == board[j][i]:
                                board[j][i]*=2
                                board[k][i] = 0
                            break
    elif dir ==1:
        for i in range(N):
            for j in range(N-1,0,-1):
                if board[j][i] != 0:
                    for k in range(j-1,-1,-1):
                        if board[k][i] != 0:
                            if board[k][i] == board[j][i]:
                                board[j][i]*=2
                                board[k][i] = 0
                            break
    elif dir == 2:
        for i in range(N):
            for j in range(N-1):
                if board[i][j] != 0:
                    for k in range(j+1,N):
                        if board[i][k] != 0:
                            if board[i][k] == board[i][j]:
                                board[i][j] *= 2
                                board[i][k] = 0
                            break
    elif dir == 3:
        for i in range(N):
            for j in range(N-1,-1,-1):
                if board[i][j] != 0:
                    for k in range(j-1,-1,-1):
                        if board[i][k] != 0:
                            if board[i][k] == board[i][j]:
                                board[i][j] *= 2
                                board[i][k] = 0
                            break
d = ['up','down','left','right']

tc = int(input())
for t in range(tc):
    N,S = input().split()
    N = int(N)
    board = [list(map(int,input().split())) for _ in range(N)]
    plus(d.index(S))
    move(d.index(S))

    print('#{}'.format(t+1))
    for i in range(N):
        print(' '.join(map(str,board[i])))








