import sys
sys.stdin = open('oselo.txt','r')
#
# tc = int(input())
# for t in range(tc):
#     N,M_su = map(int,input().split())
#     board = [['*']*N for _ in range(N)]
#     board[N//2][N//2] = 2
#     board[N//2-1][N//2-1] = 2
#     board[N//2][N//2-1] =1
#     board[N//2-1][N//2] =1
#
#     for m in range(M_su):
#         x,y,color = map(int,input().split()) #y=1 이면 판에 0번째 즉 입력은 y-1로
#
#         # board 판 보여주기
#         # for i in range(N):
#         #     print(board[i])
#         # print()
#
#         # 바둑돌 삽입
#         board[y-1][x-1] = color
#
#         #가로행 확인하기
#         for y1 in range(N):
#             for x1 in range(1,N-1):
#                 if board[y1][x1] != 1 and board[y1][x1-1] ==1 and board[y1][x1+1] == 1:
#                     board[y1][x1] =1
#                     break
#                 if board[y1][x1] != 2 and board[y1][x1-1] ==2 and board[y1][x1+1] == 2:
#                     board[y1][x1] =2
#                     break
#
#         #세로행 확인하기
#         for x in range(N):
#             for y in range(1,N-1):
#                 if board[y][x] != 1 and board[y-1][x] == 1 and board[y+1][x] == 1:
#                     board[y][x] = 1
#                     break
#                 if board[y][x] != 2 and board[y-1][x] == 2 and board[y+1][x] == 2:
#                     board[y][x] = 2
#                     break
#
#         #대각 역 대각 확인하기
#         for y in range(1,N-1):
#             for x in range(1,N-1):
#                 if board[y][x] != 1 and board[y-1][x-1] == 1 and board[y+1][x+1] == 1:
#                     board[y][x] = 1
#                     break
#                 if board[y][x] != 2 and board[y-1][x-1] == 2 and board[y+1][x+1] == 2:
#                     board[y][x] = 2
#                     break
#
#
#         # 한 턴 끝날때 마다 보드판 보여주기
#         for i in range(N):
#             print(board[i])
#         print()





        # #가운데 가로 행 확인
        # for y in range(1,N-1):
        #     for x in range(1,N-1):
        #         if board[y][x] != 1 and board[y][x-1] == 1 and board[y][x+1] == 1:
        #             board[y][x] = 1
        #         if board[y][x] != 2 and board[y][x-1] == 2 and board[y][x+1] == 2:
        #             board[y][x] = 2
        #
        # #가운데 세로 행 확인
        # for x in range(1,N-1):
        #     for y in range(1,N-1):
        #         if board[y][x] != 1 and board[y][x-1] == 1 and board[y][x+1] == 1:
        #             board[y][x] = 1
        #         if board[y][x] != 2 and board[y][x-1] == 2 and board[y][x+1] == 2:
        #             board[y][x] = 2
        #
        # # 대각선 역슬래쉬 확인
        # for y in range(1,N-1):
        #     for x in range(1,N-1):
        #         if board[y][x] != 1 and board[y-1][x-1] == 1 and board[y+1][x+1] == 1:
        #             board[y][x] =1
        #         if board[y][x] != 2 and board[y-1][x-1] == 2 and board[y+1][x+1] == 2:
        #             board[y][x] =2
        #
        # # 대각선 / 방향 확인
        # for y in range(1,N-1):
        #     for x in range(1,N-1):
        #         if board[y][x] != 1 and board[y-1][x+1] ==1 and board[y+1][x-1] == 1:
        #             board[y][x] =1
        #         if board[y][x] != 2 and board[y-1][x+1] ==2 and board[y+1][x-1] == 2:
        #             board[y][x] =2
        #


        # #한 턴 끝날때 마다 보드판 보여주기
        # for i in range(N):
        #     print(board[i])
        # print()




'''
T = int(input())
# test case의 수

delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
# 8방향 탐색을 위해 delta 선언

for t_case in range(T):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    # 입력받기

    mid = n // 2
    # mid는 현재 보드 크기 n의 절반이다.

    board[mid][mid] = 2
    board[mid - 1][mid - 1] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1
    # 초기화. 처음에 보드의 상태를 정의한다. 정중앙에 네 개의 돌이 엇갈려 놓여있다.


    for i in range(m):
        x, y, c = map(int, input().split())
        # 각각 보드위의 행, 열, 색을 저장한다.
        y, x = y - 1, x - 1
        # 문제의 좌표 표기가 1부터이므로 -1을 해준다.

        reverse = []  # 뒤집어야 할 돌을 저장할 리스트 reverse 초기화

        # 8방향 탐색
        for i in range(8):
            dx, dy = delta[i]
            nx, ny = x + dx, y + dy
            while True:
                if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:  # 모서리인가?
                    reverse = []
                    break
                if board[nx][ny] == 0:  # 빈 칸을 만난경우 reverse를 초기화
                    reverse = []
                    break
                if board[nx][ny] == c:  # 같은 색을 만났으므로 break
                    break
                else:  # 조건에 부합하는 돌을 reverse에 추가한다.
                    reverse.append((nx, ny))
                nx, ny = nx + dx, ny + dy
            for rx, ry in reverse:  # 뒤집어준다.
                if c == 1:
                    board[rx][ry] = 1
                else:
                    board[rx][ry] = 2
        board[x][y] = c

    # 각각의 돌 숫자를 세준다.
    w, b = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                w += 1
            elif board[i][j] == 2:
                b += 1

    print('#{} {} {}'.format(t_case + 1, w, b))
'''



dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]


def init():
    st = N // 2
    othello[st][st] = othello[st + 1][st + 1] = 2
    othello[st + 1][st] = othello[st][st + 1] = 1


def change(r, c, color):
    othello[r][c] = color

    for i in range(8):
        nr = r
        nc = c
        while 1:
            nr += dr[i]
            nc += dc[i]
            if nr <= 0 or nr > N or nc <= 0 or nc > N:
                break
            if othello[nr][nc] == 0:
                break
            if othello[nr][nc] == color:
                while not (nr == r and nc == c):
                    nr -= dr[i]
                    nc -= dc[i]
                    othello[nr][nc] = color
                break


def m_count(num):
    cnt = 0
    for i in range(N + 1):
        for j in range(N + 1):
            if othello[i][j] == num:
                cnt += 1
    return cnt


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    othello = [[0] * (N + 1) for _ in range(N + 1)]
    init()

    for i in range(M):
        c, r, color = map(int, input().split())
        change(r, c, color)

    b_cnt = m_count(1)
    w_cnt = m_count(2)
    print("#{} {} {}".format(tc, b_cnt, w_cnt))