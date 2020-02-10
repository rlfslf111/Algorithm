
def coordinate(num):
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == num:
                return x,y

tc = int(input())
for t in range(tc):
    one,two = map(int,input().split())
    board = [[0]*300 for _ in range(300)]
    num = 1
    for y in range(1,2):
        for x in range(1,len(board)):
            board[y][x] = num
            num += x+1


    for y in range(2,len(board)):
        for x in range(1,len(board)-1):
            if x <= 0 or x >= len(board):
                break
            board[y][x] = board[y-1][x+1] - 1

    find_su1 = coordinate(one)[0] + coordinate(two)[0]
    find_su2 = coordinate(one)[1] + coordinate(two)[1]
    print('#{} {}'.format(t+1,board[find_su2][find_su1]))

    # for i in range(len(board)):
    #     print(board[i])
    # coordinate(y,x)