import sys
sys.setrecursionlimit(1000000)

def move(spot,state):
    global cnt
    if spot == N**2:
        cnt += 1
    else:
        y = (spot-1) // N
        x = (spot-1) % N
        if state == 1:
            if x + 1 < N and house[y][x + 1] != 1:
                move(spot + 1, 1)
            if x + 1 < N and y + 1 < N and house[y + 1][x] != 1 and house[y][x + 1] != 1 and house[y + 1][x + 1] != 1:
                move(spot + N + 1, 2)
        elif state == 2:
            if x + 1 < N and house[y][x + 1] != 1:
                move(spot + 1, 1)
            if x + 1 < N and y + 1 < N and house[y + 1][x] != 1 and house[y][x + 1] != 1 and house[y + 1][x + 1] != 1:
                move(spot + N + 1, 2)
            if y + 1 < N and house[y + 1][x] != 1:
                move(spot + N, 3)
        elif state == 3:
            if x + 1 < N and y + 1 < N and house[y + 1][x] != 1 and house[y][x + 1] != 1 and house[y + 1][x + 1] != 1:
                move(spot + N + 1, 2)
            if y + 1 < N and house[y + 1][x] != 1:
                move(spot + N, 3)

N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
#state = 1 오른쪽, state = 2 대각선, state = 3 아래
start_state = 1
start_spot = 2
if house[0][2] == 1 or house[N-1][N-1] == 1:
    print(0)
elif house[N-2][N-1] == 1 and house[N-1][N-2] == 1:
    print(0)
else:
    move(start_spot,start_state)
    print(cnt)

    
    
    
#DP로 풀기
# N = int(input())
# room = [list(map(int,input().split())) for _ in range(N)]
# dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
# dp[0][1][0] = 1
#
# for i in range(N):
#     for j in range(1,N):
#         # 가로
#         if j != N - 1 and not room[i][j+1]:
#             dp[i][j+1][0] = dp[i][j][0] + dp[i][j][2]
#         # 세로
#         if i != N - 1 and not room[i+1][j]:
#             dp[i+1][j][1] = dp[i][j][1] + dp[i][j][2]
#         # 대각선
#         if j != N - 1 and i != N - 1 and not room[i][j+1] and not room[i+1][j] and not room[i+1][j+1]:
#             dp[i+1][j+1][2] = dp[i][j][0] + dp[i][j][1] + dp[i][j][2]
#
# print(sum(dp[N-1][N-1]))


