from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

hy = [-2,-1,1,2,2,1,-1,-2]
hx = [1,2,2,1,-1,-2,-2,-1]

def bfs(y,x,move,horse):
    q = deque()
    q.append((y,x,move,horse))

    while q:
        y, x, move, horse = q.popleft()
        if y == H - 1 and x == W - 1:
            return move

        # move monkey
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= H or nx < 0 or nx >= W or board[ny][nx] == 1:
                continue
            elif board[ny][nx] == 0 and visit[ny][nx][horse] == 0:
                visit[ny][nx][horse] = 1
                q.append((ny,nx,move + 1,horse))

        # move like horse
        if horse:
            for i in range(len(hy)):
                ty, tx = y + hy[i], x + hx[i]
                if ty < 0 or ty >= H or tx < 0 or tx >= W or board[ty][tx] == 1:
                    continue
                elif board[ty][tx] == 0 and visit[ty][tx][horse-1] == 0:
                    visit[ty][tx][horse-1] = 1
                    q.append((ty,tx,move + 1,horse - 1))

    return -1

K = int(input())
W, H = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(H)]
visit = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
visit[0][0][K] = 1

print(bfs(0,0,0,K))