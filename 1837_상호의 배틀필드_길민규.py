# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def shoot(y,x):
    if field[y][x] == '^':
        ny = y
        nx = x
        while 1:
            ny += dy[0]
            nx += dx[0]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                break
            if field[ny][nx] == '#':
                break
            if field[ny][nx] == '*':
                field[ny][nx] = '.'
                break
    elif field[y][x] == 'v':
        ny = y
        nx = x
        while 1:
            ny += dy[1]
            nx += dx[1]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                break
            if field[ny][nx] == '#':
                break
            if field[ny][nx] == '*':
                field[ny][nx] = '.'
                break
    elif field[y][x] == '<':
        ny = y
        nx = x
        while 1:
            ny += dy[2]
            nx += dx[2]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                break
            if field[ny][nx] == '#':
                break
            if field[ny][nx] == '*':
                field[ny][nx] = '.'
                break
    elif field[y][x] == '>':
        ny = y
        nx = x
        while 1:
            ny += dy[3]
            nx += dx[3]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                break
            if field[ny][nx] == '#':
                break
            if field[ny][nx] == '*':
                field[ny][nx] = '.'
                break

def up(y,x):
    ny = y + dy[0]
    nx = x + dx[0]
    if ny < 0 or ny >= H or nx < 0 or nx >= W:
        field[y][x] = '^'
        return (y,x)
    if field[ny][nx] == '-' or field[ny][nx] == '#' or field[ny][nx] == '*':
        field[y][x] = '^'
        return (y,x)
    if field[ny][nx] == '.':
        field[y][x] = '.'
        field[ny][nx] = '^'
        return (ny,nx)

def down(y,x):
    ny = y + dy[1]
    nx = x + dx[1]
    if ny < 0 or ny >= H or nx < 0 or nx >= W:
        field[y][x] = 'v'
        return (y,x)
    if field[ny][nx] == '-' or field[ny][nx] == '#' or field[ny][nx] == '*':
        field[y][x] = 'v'
        return (y,x)
    if field[ny][nx] == '.':
        field[y][x] = '.'
        field[ny][nx] = 'v'
        return (ny, nx)

def left(y,x):
    ny = y + dy[2]
    nx = x + dx[2]
    if ny < 0 or ny >= H or nx < 0 or nx >= W:
        field[y][x] = '<'
        return (y,x)
    if field[ny][nx] == '-' or field[ny][nx] == '#' or field[ny][nx] == '*':
        field[y][x] = '<'
        return (y,x)
    if field[ny][nx] == '.':
        field[y][x] = '.'
        field[ny][nx] = '<'
        return (ny, nx)

def right(y,x):
    ny = y + dy[3]
    nx = x + dx[3]
    if ny < 0 or ny >= H or nx < 0 or nx >= W:
        field[y][x] = '>'
        return (y,x)
    if field[ny][nx] == '-' or field[ny][nx] == '#' or field[ny][nx] == '*':
        field[y][x] = '>'
        return (y,x)
    if field[ny][nx] == '.':
        field[y][x] = '.'
        field[ny][nx] = '>'
        return (ny, nx)

tc = int(input())
for t in range(tc):
    H, W = map(int,input().split())
    field = [list(input()) for _ in range(H)]
    order_seq = int(input())
    order = list(input())

    for y1 in range(H):
        for x1 in range(W):
            if field[y1][x1] == '<' or field[y1][x1] == '>' or field[y1][x1] == '^' or field[y1][x1] == 'v':
                y_in = y1
                x_in = x1

    y, x = y_in, x_in
    for i in range(order_seq):
            if field[y][x] == '<' or field[y][x] == '>' or field[y][x] == '^' or field[y][x] == 'v':
                if order[i] == 'S':
                    shoot(y,x)
                if order[i] == 'U':
                    coord = up(y,x)
                    y, x = coord[0], coord[1]
                if order[i] == 'D':
                    coord = down(y,x)
                    y, x = coord[0], coord[1]
                if order[i] == 'L':
                    coord = left(y,x)
                    y, x = coord[0], coord[1]
                if order[i] == 'R':
                    coord = right(y,x)
                    y, x = coord[0], coord[1]

    print('#{}'.format(t+1),end=' ')
    for f in range(H):
        print('{}'.format(''.join(map(str,field[f]))))
