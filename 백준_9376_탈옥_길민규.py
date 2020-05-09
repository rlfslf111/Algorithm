from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(y,x):
    board = [[-1]*(w+2) for _ in range(h+2)]
    run = deque()
    run.append((y,x))
    board[y][x] = 0
    while run:
        y,x = run.popleft()
        for i in range(len(dy)):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= h+2 or nx < 0 or nx >= w+2 or jail[ny][nx] == '*':
                continue
            if board[ny][nx] >= 0:
                continue
            if jail[ny][nx] == '.':
                board[ny][nx] = board[y][x]
                # 원래 map 범위 밖의 좌표가 문을 여는 마지막 곳을 덮을 수 있으므로 앞으로 추가한다.
                run.appendleft((ny,nx))
            elif jail[ny][nx] == '#':
                board[ny][nx] = board[y][x] + 1
                run.append((ny,nx))
    return board

for _ in range(int(input())):
    h, w = map(int,input().split())
    # 양 측벽으로 1칸씩 확장
    jail = ['.'*(w+2)]
    for _ in range(h):
        jail.append(list('.'+ input() + '.'))
    jail.append(list('.'*(w+2)))

    q = deque()
    for i in range(h+2):
        for j in range(w+2):
            if jail[i][j] == '$':
                jail[i][j] = '.'
                q.append((i,j))

    # 첫 번째 죄수의 탈출 경로
    cy1, cx1 = q.popleft()
    d1= bfs(cy1, cx1)

    # 두 번째 죄수의 탈출 경로
    cy2, cx2 = q.popleft()
    d2 = bfs(cy2, cx2)

    # 원점에서의 죄수까지의 필요한 문의 갯수
    d3 = bfs(0,0)

    minv = 1231231

    for y in range(h+2):
        for x in range(w+2):
            if jail[y][x] == '*':
                continue
            ans = d1[y][x] + d2[y][x] + d3[y][x]
            if jail[y][x] == '#':
                ans -= 2
            minv = min(ans,minv)

    print(minv)
