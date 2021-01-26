N, M = map(int,input().split())
board = [input() for _ in range(N)]
ans = 1231231
compare1 = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
compare2 = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
# board를 8*8로 자르기
for i in range(N-7):
    for j in range(M-7):
        # 8*8 시작 point
        change1 = 0
        change2 = 0
        for y in range(8):
            for x in range(8):
                # compare1
                if board[i + y][j + x] != compare1[y][x]:
                    change1 += 1
                if board[i + y][j + x] != compare2[y][x]:
                    change2 += 1


        ans = min(ans, change1, change2)

print(ans)

