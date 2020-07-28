import sys
input = sys.stdin.readline

from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(y,x,color):
    puyo = deque()
    puyo.append((y,x,color))
    check[y][x] = 1
    while puyo:
        y, x, color = puyo.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= 12 or nx < 0 or nx >= 6 or board[ny][nx] == '.':
                continue
            elif check[ny][nx] != 1 and color == board[ny][nx]:
                puyo.append((ny,nx,board[ny][nx]))
                check[ny][nx] = 1
                target.append((ny,nx))

def gravity():
    for y in range(11,-1,-1):
        for x in range(5,-1,-1):
            if board[y][x] == '.':
                for i in range(y,-1,-1):
                    if board[i][x] != '.':
                        board[y][x] = board[i][x]
                        board[i][x] = '.'
                        break

board = []
for i in range(12):
    board.append(list(input().strip()))

check = [[0 for _ in range(6)] for _ in range(12)]
count = 0

while 1:
    remove = []
    for y in range(12):
        for x in range(6):
            if not check[y][x] and board[y][x] != '.':
                target = [(y,x)]
                bfs(y,x,board[y][x])
                if len(target) >= 4:
                    for i in range(len(target)):
                        remove.append(target[i])
    if len(remove) == 0:
        break
    else:
        for i in range(len(remove)):
            board[remove[i][0]][remove[i][1]] = '.'
        check = [[0 for _ in range(6)] for _ in range(12)]
        count += 1

    gravity()
print(count)
