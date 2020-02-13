dx = [-1,1]
def dir_check(y,x):
    for i in range(len(dx)):
        nx = x+dx[i]
        if nx < 0 or nx >= 100:
            continue
        if ladder[y][nx] == 1:
            return i
    return 2

def go(st):
    x_chuk = st
    for i in range(100):
        dir = dir_check(i,x_chuk)
        if dir < 2:
            while 1:
                nx = x_chuk+dx[dir]
                if nx < 0 or nx >= 100 or ladder[i][nx] == 0:
                    break
                x_chuk = nx
        if ladder[i][x_chuk] == 2:
            return st
    return 0
for t in range(10):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]


    for i in range(100):
        if ladder[0][i] == 1:
            temp = go(i)
            if temp:
                print('#{} {}'.format(tc,temp))