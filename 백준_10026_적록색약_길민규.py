import sys
sys.setrecursionlimit(100000)

dy = [0,-1, 0, 1, 0]
dx = [0,0, 1, 0, -1]

def see_R(y, x):
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] != 'R':
            continue
        if board[ny][nx] == 'R':
            board[ny][nx] = 'T'
            see_R(ny, nx)

def see_B(y, x):
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] != 'B':
            continue
        if board[ny][nx] == 'B':
            board[ny][nx] = 'L'
            see_B(ny, nx)

def see_G(y, x):
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] != 'G':
            continue
        if board[ny][nx] == 'G':
            board[ny][nx] = 'T'
            see_G(ny, nx)

def see_RG(y, x):
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] != 'T':
            continue
        if board[ny][nx] == 'T':
            board[ny][nx] = 'X'
            see_RG(ny, nx)

N = int(input())
board = [list(input()) for _ in range(N)]

cnt = 0
cnt_RG = 0

# 정상인 사람이 봤을 때
for y in range(N):
    for x in range(N):
        if board[y][x] == 'R':
            see_R(y, x)
            cnt += 1
        if board[y][x] == 'B':
            see_B(y, x)
            cnt += 1
            cnt_RG += 1
        if board[y][x] == 'G':
            see_G(y, x)
            cnt += 1

# 적록 색약인 사람이 봤을 때
for y in range(N):
    for x in range(N):
        if board[y][x] == 'T':
            see_RG(y, x)
            cnt_RG += 1

print(cnt,cnt_RG)