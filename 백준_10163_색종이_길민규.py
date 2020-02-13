N = int(input())
board = [[0]*101 for _ in range(101)]
for n in range(N):
    i1,j1,width,height = map(int,input().split())

    for y in range(i1,i1+width):
        for x in range(j1,j1+height):
            board[y][x] = n+1


for n in range(N):
    count = 0
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == n+1:
                count+=1
    print(count)