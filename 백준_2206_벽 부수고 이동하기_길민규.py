from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs():
    q = deque()
    q.append((0,0,0))
    while q:
        y, x, z = q.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                # 벽을 부수지 않고 이동하거나(z == 0), 벽을 부순 상태로 이동(z == 1)
                if board[ny][nx] == 0 and check[ny][nx][z] == -1:
                    check[ny][nx][z] = check[y][x][z] + 1
                    q.append((ny,nx,z))

                # 벽을 한번도 부수지 않은 상태에서 벽을 한 번 만날 경우
                if z == 0 and board[ny][nx] == 1 and check[ny][nx][z] == -1:
                    check[ny][nx][z+1] = check[y][x][z] + 1
                    q.append((ny,nx,z+1))

    # 벽을 부수고 갔을 때만 존재할 때
    if check[N-1][M-1][0] == -1:
        return check[N-1][M-1][1]
    # 벽을 부수지 않고 갔을 때만 존재할 때
    elif check[N-1][M-1][1] == -1:
        return check[N-1][M-1][0]
    # 두 경우가 모두 존재할 때, 최솟값 return
    else:
        return min(check[N-1][M-1])


N, M = map(int,input().split())
board = [list(map(int,list(input()))) for _ in range(N)]
# 벽을 부순 상태로 움직이는지, 아닌지를 구별할 2개의 칸을 만든다.
check = [[[-1]*2 for _ in range(M)] for _ in range(N)]
# 시작 count는 1부터 시작해야 하므로 1로 초기화
check[0][0][0] = 1
print(bfs())
