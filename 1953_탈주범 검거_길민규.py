import sys
sys.stdin = open('input.txt','r')

# 상, 우, 하, 좌 순으로 이동
dy = [-1,0,1,0]
dx = [0,1,0,-1]

dy2 = [-1,1]
dx2 = [-1,1]
def run1(k,y,x,shape,idx):
    if k > L:
        return
    else:
        result.append((y,x))
        if shape == 1:
            for i in range(len(dy)):
                # 위 볼 때
                if i == 0:
                    ny = y + (-1)
                    if idx == 2 or ny < 0 or ny >= N or under[ny][x] == 0 or under[ny][x] == 3 or under[ny][x] == 4 or under[ny][x] == 7:
                        continue
                    run1(k+1,ny,x,under[ny][x],0)
                # 오른쪽 볼 때
                if i == 1:
                    nx = x + 1
                    if idx == 3 or nx < 0 or nx >= M or under[y][nx] == 0 or under[y][nx] == 2 or under[y][nx] == 4 or under[y][nx] == 5:
                        continue
                    run1(k + 1, y, nx, under[y][nx], 1)
                # 아래를 볼 때
                if i == 2:
                    ny = y + 1
                    if idx == 0 or ny < 0 or ny >= N or under[ny][x] == 0 or under[ny][x] == 3 or under[ny][x] == 5 or under[ny][x] == 6:
                        continue
                    run1(k + 1, ny, x, under[ny][x], 2)
                # 왼쪽을 볼 때
                if i == 3:
                    nx = x + (-1)
                    if idx == 1 or nx < 0 or nx >= M or under[y][nx] == 0 or under[y][nx] == 2 or under[y][nx] == 6 or under[y][nx] == 7:
                        continue
                    run1(k + 1, y, nx, under[y][nx], 3)

        elif shape == 2:
            for i in range(len(dy2)):
                # 위 볼 때
                if i == 0:
                    ny = y + (-1)
                    if idx == 2 or ny < 0 or ny >= N or under[ny][x] == 0 or under[ny][x] == 4 or under[ny][x] == 3 or under[ny][x] == 7:
                        continue
                    run1(k+1,ny,x,under[ny][x],0)

                # 아래 볼 때
                elif i == 1:
                    ny = y + 1
                    if idx == 0 or ny < 0 or ny >= N or under[ny][x] == 0 or under[ny][x] == 3 or under[ny][x] == 5 or under[ny][x] == 6:
                        continue
                    run1(k+1,ny,x,under[ny][x],2)

        elif shape == 3:
            for i in range(len(dx2)):
                # 왼쪽 볼 때
                if i == 0:
                    nx = x + (-1)
                    if idx == 1 or nx < 0 or nx >= M or under[y][nx] == 0 or under[y][nx] == 2 or under[y][nx] == 6 or under[y][nx] == 7:
                        continue
                    run1(k+1,y,nx,under[y][nx],3)

                # 오른쪽 볼 때
                elif i == 1:
                    nx = x + 1
                    if idx == 3 or nx < 0 or nx >= M or under[y][nx] == 0 or under[y][nx] == 2 or under[y][nx] == 4 or under[y][nx] == 5:
                        continue
                    run1(k+1,y,nx,under[y][nx],1)

        elif shape == 4:
            for i in range(2):
                # 위를 볼 때
                if i == 0:
                    ny = y + (-1)
                    if idx == 2 or ny < 0 or ny >= N or under[ny][x] == 0 or under[ny][x] == 3 or under[ny][x] == 7 or under[ny][x] == 4:
                        continue
                    run1(k+1,ny,x,under[ny][x],0)

                # 오른쪽을 볼 때
                elif i == 1:
                    nx = x + 1
                    if idx == 3 or nx < 0 or nx >= M or under[y][nx] == 0 or under[y][nx] == 2 or under[y][nx] == 5 or under[y][nx] == 4:
                        continue
                    run1(k+1,y,nx,under[y][nx],1)

        elif shape == 5:
            for i in range(2):
                # 오른쪽 볼 때
                if i == 0:
                    nx = x + 1
                    if idx == 3 or nx < 0 or nx >= M or under[y][nx] == 0 or under[y][nx] == 2 or under[y][nx] == 4 or under[y][nx] == 5:
                        continue
                    run1(k+1,y,nx,under[y][nx],1)

                # 아래를 볼 때
                elif i == 1:
                    ny = y + 1
                    if idx == 0 or ny < 0 or ny >= N or under[ny][x] == 0 or under[ny][x] == 3 or under[ny][x] == 6 or under[ny][x] == 5:
                        continue
                    run1(k+1,ny,x,under[ny][x],2)

        elif shape == 6:
            for i in range(2):
                #왼쪽을 볼 때
                if i == 0:
                    nx = x + (-1)
                    if idx == 1 or nx < 0 or nx >= M or under[y][nx] == 0 or under[y][nx] == 2 or under[y][nx] == 7 or under[y][nx] == 6:
                        continue
                    run1(k + 1, y, nx, under[y][nx],3)

                # 아래를 볼 때
                elif i == 1:
                    ny = y + 1
                    if idx == 0 or ny < 0 or ny >= N or under[ny][x] == 0 or under[ny][x] == 3 or under[ny][x] == 6 or under[ny][x] == 5:
                        continue
                    run1(k + 1, ny, x, under[ny][x],2)

        elif shape == 7:
            for i in range(2):
                # 위를 볼 때
                if i == 0:
                    ny = y + (-1)
                    if idx == 2 or ny < 0 or ny >= N or under[ny][x] == 0 or under[ny][x] == 3 or under[ny][x] == 4 or under[ny][x] == 7:
                        continue
                    run1(k + 1, ny, x, under[ny][x],0)

                # 왼쪽을 볼 때
                elif i == 1:
                    nx = x + (-1)
                    if idx == 1 or nx < 0 or nx >= M or under[y][nx] == 0 or under[y][nx] == 2 or under[y][nx] == 6 or under[y][nx] == 7:
                        continue
                    run1(k + 1, y, nx, under[y][nx],3)

tc = int(input())
for t in range(1,tc+1):
    N, M, R, C, L = map(int,input().split())
    under = [list(map(int,input().split())) for _ in range(N)]
    result = list()
    start_shape = under[R][C]
    run1(1,R,C,start_shape,-1)

    result = set(result)
    print('#{} {}'.format(t,len(result)))
