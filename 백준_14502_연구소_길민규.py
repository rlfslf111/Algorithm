from collections import deque
from copy import deepcopy

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs(ans):
    copy = deepcopy(board)
    q = deque()
    for i in range(len(ans)):
        r, c = ans[i][0], ans[i][1]
        copy[r][c] = 1
    for i in range(N):
        for j in range(M):
            if copy[i][j] == 2:
                q.append((i,j))

    while q:
        y, x = q.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M or copy[ny][nx] == 1:
                continue
            if copy[ny][nx] == 0:
                copy[ny][nx] = 2
                q.append((ny,nx))

    # 안전 영역 세기
    cnt = 0
    for i in range(N):
        cnt += copy[i].count(0)
    cnt_safe[0] = max(cnt,cnt_safe[0])

def perm(k):
    if k == 3:
        bfs(ans)
        return
    else:
        for i in range(len(zero)):
            if not check[i]:
                check[i] = True
                ans.append(zero[i])
                perm(k+1)
                ans.pop()
                for j in range(i+1,len(zero)):
                    check[j] = False

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
copy = deepcopy(board)
cnt_safe = [0]

# 0 을 넣어 놓는다.
zero = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            zero.append([y,x])

check = [False] * len(zero)
ans = []
perm(0)
print(cnt_safe[0])