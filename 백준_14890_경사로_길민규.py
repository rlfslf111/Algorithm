def check(road):
    cur_h = road[0]
    visit = [0] * N

    for h in range(N):

        # 길의 높이가 같으면 pass
        if cur_h == road[h]:
            continue

        # 오르막길 검사 (지나온 길이가 L 이상일 경우 가능)
        elif cur_h + 1 == road[h]:
            for k in range(h-1,h-1-L,-1):
                if k < 0 or cur_h != road[k] or visit[k] == 1:
                    return 0
                visit[k] = 1
            cur_h = road[h]

        # 내리막길 검사 (앞으로 갈 수 있는 길이가 L 이상일 경우 가능)
        elif cur_h - 1 == road[h]:
            for k in range(h,h+L):
                if k >= N or road[h] != road[k] or visit == 1:
                    return 0
                visit[k] = 1
            cur_h = road[h]

        # 그 외 경사가 1 이상의 높이인 경우
        elif abs(cur_h-road[h]) > 1:
            return 0

    return 1

N, L = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

ans = 0
#가로축 모두 확인
for i in range(N):
    ans += check(board[i])

#세로축 모두 확인
for i in range(N):
    sero = []
    for j in range(N):
        sero.append(board[j][i])
    ans += check(sero)

print(ans)