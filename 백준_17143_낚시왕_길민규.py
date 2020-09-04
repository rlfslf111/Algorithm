import sys

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def move_shark(y, x, shark):
    speed, dir, size = shark
    #시작부터 방향을 반대로 바꿔줘야 하는 경우 (런타임 에러 방지)
    if y == 0 and dir == 0:
        dir = 1
    elif y == R-1 and dir == 1:
        dir = 0
    elif x == 0 and dir == 3:
        dir = 2
    elif x == C - 1 and dir == 2:
        dir = 3
    # 위 아래로 움직이는 경우
    if dir == 0 or dir == 1:
        # speed 시간 줄이기
        speed %= ((2 * R) - 2)
        for i in range(speed):
            y += dy[dir]
            x += dx[dir]
            if y <= 0 or y >= R - 1:
                if dir == 0:
                    dir = 1
                elif dir == 1:
                    dir = 0

    # 좌우로 움직이는 경우
    elif dir == 2 or dir == 3:
        # speed 시간 줄이기
        speed %= ((2 * C) - 2)
        for i in range(speed):
            y += dy[dir]
            x += dx[dir]
            if x <= 0 or x >= C - 1:
                if dir == 2:
                    dir = 3
                elif dir == 3:
                    dir = 2

    return y, x, speed, dir, size


R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]
for m in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = [s, d - 1, z]

stand = -1
fishing_size = 0

while 1:
    # 낚시왕이 오른쪽으로 한 칸 이동
    stand += 1
    if stand == C:
        break

    # 같은 열에 상어가 있다면, 낚시왕이 포획한다.
    for y in range(R):
        if type(board[y][stand]) == list:
            fishing_size += board[y][stand][2]
            board[y][stand] = 0
            # 가장 가까운 상어만 잡는다.
            break

    # 상어들이 움진인다.
    temp_board = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if type(board[y][x]) == list:
                i, j, speed, direction, size = move_shark(y, x, board[y][x])
                board[y][x] = 0
                # 움직인 자리에 상어가 이미 있다면,
                if type(temp_board[i][j]) == list:
                    post_speed = temp_board[i][j][0]
                    post_direction = temp_board[i][j][1]
                    post_size = temp_board[i][j][2]
                    if size > post_size:
                        temp_board[i][j] = [speed, direction, size]
                    else:
                        temp_board[i][j] = [post_speed, post_direction, post_size]
                # 움직인 자리에 상어가 없으면,
                else:
                    temp_board[i][j] = [speed, direction, size]

    for y in range(R):
        for x in range(C):
            board[y][x] = temp_board[y][x]

print(fishing_size)
