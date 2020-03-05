import sys
sys.stdin = open('input.txt','r')

from collections import deque

MXN, MAXW, MAXH = 4, 12, 15

def solve(k, cur):
    global ans
    if ans == 0:
        return
    if k == N:
        cnt = 0
        for i in range(W):
            for j in range(H):
                if cur[j][i]:
                    cnt += 1
        ans = min(ans, cnt)
    else:
        for y in range(W):
            next = [[0] * W for _ in range(H)]
            visit = [[False] * W for _ in range(H)]
            Q = deque()
            x = 0
            while x < H:
                if cur[x][y]:
                    visit[x][y] = True
                    Q.append((x, y))
                    break
                x += 1
            if x == H:
                continue

            while Q:
                tx, ty = Q.popleft()
                fr = max(0, tx - cur[tx][ty] + 1)
                to = min(tx + cur[tx][ty] - 1, H - 1)

                for j in range(fr, to + 1):
                    if visit[j][ty] or cur[j][ty] == 0:
                        continue
                    visit[j][ty] = True
                    if cur[j][ty] > 1:
                        Q.append((j, ty))

                fr = max(0, ty - cur[tx][ty] + 1)
                to = min(ty + cur[tx][ty] - 1, W - 1)

                for j in range(fr, to + 1):
                    if visit[tx][j] or cur[tx][j] == 0:
                        continue
                    visit[tx][j] = True
                    if cur[tx][j] > 1:
                        Q.append((tx, j))

            # 정리하기
            remain = 0
            for i in range(W):
                idx = H - 1
                for j in range(H - 1, -1, -1):
                    if visit[j][i] or cur[j][i] == 0:
                        continue
                    next[idx][i] = cur[j][i]
                    idx, remain = idx - 1, remain + 1
            if remain == 0:
                ans = remain
                return

            solve(k + 1, next)


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    cur = [list(map(int, input().split())) for _ in range(H)]

    ans = 0xfffff
    solve(0, cur)
    print('#{} {}'.format(tc, ans))