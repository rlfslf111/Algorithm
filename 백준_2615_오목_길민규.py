dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

def verify_white(y,x):
    count_list = []
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        count = 1
        if ny < 0 or ny >= 19 or nx < 0 or nx >= 19:
            continue
        if board[ny][nx] == 2:
            while 1:
                ny += dy[i]
                nx += dx[i]
                count += 1
                if ny < 0 or ny >= 19 or nx < 0 or nx >= 19:
                    break
                if board[ny][nx] != 2:
                    break
        if count == 6:
            while 1:
                if ny < 0 or ny >= 19 or nx < 0 or nx >= 19:
                    break
                ny -= dy[i]
                nx -= dx[i]
                board[ny][nx] = 0
        count_list.append(count)
    return count_list

def verify_black(y,x):
    count_list = []
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        count = 1
        if ny < 0 or ny >= 19 or nx < 0 or nx >= 19:
            continue
        if board[ny][nx] == 1:
            while 1:
                ny += dy[i]
                nx += dx[i]
                count += 1
                if ny < 0 or ny >= 19 or nx < 0 or nx >= 19:
                    break
                if board[ny][nx] != 1:
                    break
        if count == 6:
            while 1:
                if ny < 0 or ny >= 19 or nx < 0 or nx >= 19:
                    break
                ny -= dy[i]
                nx -= dx[i]
                board[ny][nx] = 0
        count_list.append(count)
    return count_list

board = [list(map(int,input().split())) for _ in range(19)]

white_list = []
black_list = []

white_spot = []
black_spot = []

for x in range(19):
    for y in range(19):
        if board[y][x] == 2:
            white_spot.append([y+1,x+1])
            white_list.append(verify_white(y,x))

        if board[y][x] == 1:
            black_spot.append([y+1,x+1])
            black_list.append(verify_black(y,x))

flag = False

for i in range(len(white_list)):
    if 5 in white_list[i]:
        flag = True
        if flag:
            print(2)
            print(*white_spot[i])
            break

for i in range(len(black_list)):
    if 5 in black_list[i]:
        flag = True
        if flag:
            print(1)
            print(*black_spot[i])
            break

if not flag:
    print(0)






# import sys
#
# dx = [0, 1, 1, 1]
# dy = [1, 0, -1, 1]
# black = []
# white = []
# for i in range(1, 20):
#     board = list(map(int, input().split()))
#     for j in range(len(board)):
#         if board[j] == 1:
#             black.append([i, j + 1])
#         elif board[j] == 2:
#             white.append([i, j + 1])
# # black부터 찾아보자
# for b1 in black:
#     r, c = b1
#     for d in range(4):
#         check_r, check_c = r, c
#         cnt = 1
#         while 0 <= check_r <= 19 and 0 <= check_c <= 19:
#             if [check_r + dx[d], check_c + dy[d]] in black:
#                 cnt += 1
#                 check_r += dx[d];
#                 check_c += dy[d]
#             else:
#                 break
#             if cnt >= 5:
#                 break
#         if cnt == 5:
#             if [check_r + dx[d], check_c + dy[d]] not in black:
#                 if 1 <= r - dx[d] <= 19 and 1 <= c - dy[d] <= 19:
#                     if [r - dx[d], c - dy[d]] not in black:
#                         if d != 2:
#                             print(1)
#                             print(r, c)
#                             sys.exit()
#                         else:
#                             print(1)
#                             print(check_r, check_c)
#                             sys.exit()
#                 else:
#                     if d != 2:
#                         print(1);
#                         print(r, c), sys.exit()
#                     else:
#                         print(1);
#                         print(check_r, check_c), sys.exit()
#
# # white를 찾아보자
# for b1 in white:
#     r, c = b1
#     for d in range(4):
#         check_r, check_c = r, c
#         cnt = 1
#         while 0 <= check_r <= 19 and 0 <= check_c <= 19:
#             if [check_r + dx[d], check_c + dy[d]] in white:
#                 cnt += 1
#                 check_r += dx[d];
#                 check_c += dy[d]
#             else:
#                 break
#             if cnt >= 5:
#                 break
#         if cnt == 5:
#             if [check_r + dx[d], check_c + dy[d]] not in white:
#                 if 1 <= r - dx[d] <= 19 and 1 <= c - dy[d] <= 19:
#                     if [r - dx[d], c - dy[d]] not in white:
#                         if d != 2:
#                             print(2)
#                             print(r, c)
#                             sys.exit()
#                         else:
#                             print(2);
#                             print(check_r, check_c);
#                             sys.exit()
#                 else:
#                     if d != 2:
#                         print(2);
#                         print(r, c), sys.exit()
#                     else:
#                         print(2);
#                         print(check_r, check_c);
#                         sys.exit()
#
# print(0)