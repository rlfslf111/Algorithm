N = int(input())
K = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
# 사과 위치
for k in range(K):
    r,c = map(int,input().split())
    board[r][c] = 1

# 초, 이동방향
L = int(input())
order = []
for l in range(L):
    X, C = input().split()
    order.append([int(X),C])

move_stack = [[1,1]]

time = 0
idx = 0
# dir = 0, 1, 2, 3  상 우 하 좌
dir = 1
y, x = 1, 1
dy = [-1,0,1,0]
dx = [0,1,0,-1]
while 1:
    if idx < len(order) and time == order[idx][0]:
        if order[idx][1] == 'L':
            dir -= 1
            idx += 1
            if dir < 0:
                dir = 3
        elif order[idx][1] == 'D':
            dir += 1
            idx += 1
            if dir > 3:
                dir = 0

    else:
        ty = y + dy[dir]
        tx = x + dx[dir]
        if ty <= 0 or ty > N or tx <= 0 or tx > N or [ty,tx] in move_stack:
            break
        move_stack.append([ty,tx])
        if board[ty][tx] == 0:
            del move_stack[0]
        board[ty][tx] = 0
        y, x = ty, tx

        time += 1
print(time+1)
