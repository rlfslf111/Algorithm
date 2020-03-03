import sys
sys.stdin = open('input.txt','r')

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def move(y,x):
    visit[y][x] = 1
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if num[ny][nx] - num[y][x] == 1:
            cnt[0] += 1
            move(ny,nx)

tc = int(input())
for t in range(1,tc+1):
    N = int(input())
    num = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    cnt = [1]
    value = []
    number = []

    for y in range(N):
        for x in range(N):
            if visit[y][x]:
                continue
            move(y,x)
            value.append(cnt[0])
            number.append(num[y][x])
            cnt[0] = 1

    max_value = max(value)
    max_number = []
    for i in range(len(value)):
        if value[i] == max_value:
            max_number.append(number[i])
    print('#{} {} {}'.format(t,min(max_number),max_value))