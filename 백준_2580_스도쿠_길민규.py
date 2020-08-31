import sys
input = sys.stdin.readline

# 가로 검사
def horizon_verify(y,num):
    if num in board[y]:
        return False
    return True

# 세로 검사
def vertical_verify(x,num):
    for i in range(9):
        if num == board[i][x]:
            return False
    return True

# 3x3 검사
def square_verify(y,x,num):
    ny = y//3 * 3
    nx = x//3 * 3
    for i in range(3):
        for j in range(3):
            if board[ny + i][nx + j] == num:
                return False
    return True

# 채우기
def fill(depth):
    # 이미 답이 나와있는 경우 return처리
    if flag[0]:
        return
    if depth == len(blank):
        for y in range(9):
            for x in range(9):
                print(board[y][x], end=' ')
            print()
        flag[0] = True
        return
    else:
        for num in range(1,10):
            if horizon_verify(blank[depth][0],num) and vertical_verify(blank[depth][1],num) and square_verify(blank[depth][0],blank[depth][1],num):
                board[blank[depth][0]][blank[depth][1]] = num
                fill(depth + 1)
                board[blank[depth][0]][blank[depth][1]] = 0

board = []
blank = []
for i in range(9):
    board.append(list(map(int,input().split())))
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i,j))

flag = [False]
fill(0)