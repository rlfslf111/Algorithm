dy = [0,1,-1,0,0]
dx = [0,0,0,-1,1]
def home(y,x):
    global cnt
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if apart[ny][nx] == 1:
            apart[ny][nx] = 4
            cnt += 1
            home(ny,nx)

N = int(input())
apart = [list(map(int,list(input()))) for _ in range(N)]

ans = 0
cnt_list = []
for y in range(N):
    for x in range(N):
        cnt = 0
        if apart[y][x] == 1:
            home(y,x)
            cnt_list.append(cnt)
            ans += 1

cnt_list.sort()
print(ans)
for x in cnt_list:
    print(x)