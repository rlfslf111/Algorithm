import sys
sys.stdin = open('input.txt','r')

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y,x):
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if board[ny][nx] != 0:
            board[ny][nx] = 0
            dfs(ny,nx)

def find(y,x):
    cnt_r = 1
    cnt_c = 1
    ny = y
    nx = x
    while 1:
        ny += dy[1]
        nx += dx[1]
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == 0:
            break
        if board[ny][nx] != 0:
            cnt_c += 1

    ny = y
    nx = x
    while 1:
        ny += dy[2]
        nx += dx[2]
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == 0:
            break
        if board[ny][nx] != 0:
            cnt_r += 1
    dfs(y,x)
    return cnt_r, cnt_c

def area_sort(ans):
    for i in range(len(ans)):
        for j in range(len(ans)-1-i):
            if ans[j][0]*ans[j][1] > ans[j+1][0]*ans[j+1][1]:
                ans[j], ans[j+1] = ans[j+1], ans[j]
            if ans[j][0]*ans[j][1] == ans[j+1][0]*ans[j+1][1]:
                if ans[j][0] > ans[j+1][0]:
                    ans[j], ans[j+1] = ans[j+1], ans[j]

tc = int(input())
for t in range(1,tc+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]

    ans = []
    cnt = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] != 0:
                ans.append(find(y,x))
                cnt += 1
    area_sort(ans)

    result = [str(cnt)]
    for c in range(len(ans)):
        for r in range(len(ans[c])):
            result.append(str(ans[c][r]))
    print('#{} {}'.format(t,' '.join(result)))
