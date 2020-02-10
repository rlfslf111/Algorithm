# dy = [-2, -1, 0, 1, 2, 1, 0, -1]
# dx = [0, 1, 2, 1, 0, -1, -2, -1]
#
# tc = int(input())
# for t in range(1,tc+1):
#     word = input()
#
#     board = [['.']*(4*len(word)+1) for _ in range(5)]
#     for i in range(len(word)):
#         row = 2
#         col = 2 + (4*i)
#         board[row][col] = word[i]
#
#         for k in range(8):
#             ny = row + dy[k]
#             nx = col + dx[k]
#             board[ny][nx] = '#'
#
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             print('{}'.format(board[i][j]),end='')
#         print()





dy = [-2, -1, 0, 1, 2, 1, 0, -1]
dx = [0, 1, 2, 1, 0, -1, -2, -1]

tc = int(input())
for t in range(tc):
    word = input()

    white_board = [['.'] * (4*len(word)+1) for _ in range(5)]

    for gul in range(len(word)):
        y_chuk = 2
        x_chuk = 2 + (4*gul)
        white_board[y_chuk][x_chuk] = word[gul]

        for move in range(len(dy)):
            move_y = y_chuk + dy[move]
            move_x = x_chuk + dx[move]
            white_board[move_y][move_x] = '#'

    for x in range(len(white_board)):
        print(''.join(map(str,white_board[x])))


























