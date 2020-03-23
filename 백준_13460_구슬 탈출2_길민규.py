from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def tilt(y, x, dy, dx):
    cnt = 0
    # 다음으로 갈 곳이 벽이 아니거나, 아웃이 아니면 계속 움직인다.
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt

def escape():
    while q:
        ry, rx, by, bx, move = q.popleft()
        # 10회 이상을 수행할 시 break
        if move > 10:
            break
        for i in range(len(dy)):
            # red의 다음 좌표
            nry, nrx, rcnt = tilt(ry,rx,dy[i],dx[i])
            # blue의 다음 좌표
            nby, nbx, bcnt = tilt(by,bx,dy[i],dx[i])

            # 실패 조건이 아닌, blue가 out이 아니라면,
            if board[nby][nbx] != 'O':
                # red가 out이 되면 move를 return
                if board[nry][nrx] == 'O':
                    print(move)
                    return
                # red와 blue가 겹친다면, 움직인 거리가 더 많은 색을 한칸 뒤로
                if nry == nby and nrx == nbx:
                    if rcnt > bcnt:
                        nry -= dy[i]
                        nrx -= dx[i]
                    else:
                        nby -= dy[i]
                        nbx -= dx[i]
                # red와 blue의 위치가 전에 있었던 곳인지 중복체크
                if not check[nry][nrx][nby][nbx]:
                    check[nry][nrx][nby][nbx] = True
                    q.append((nry,nrx,nby,nbx,move+1))
    print(-1)

N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
# red와 blue가 있을 수 있는 자리를 동시에 check
check = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

q = deque()
cry, crx, cby, cbx = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            cry, crx = i, j
        if board[i][j] == 'B':
            cby, cbx = i, j
# q에 depth 1을 넣어준다.
q.append((cry, crx, cby, cbx, 1))
# 첫 번째로 놓여져 있던 자리를 True로
check[cry][crx][cby][cbx] = True
escape()

