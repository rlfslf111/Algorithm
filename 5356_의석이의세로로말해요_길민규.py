import sys
sys.stdin = open('length.txt','r')

tc = int(input())
for t in range(tc):
    word = [list(input()) for _ in range(5)]

    board = [['*']*15 for _ in range(15)]
    for y in range(len(word)):
        for x in range(len(word[y])):
            board[y][x]=word[y][x]

    ans = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] == '*':
                continue
            ans.append(board[y][x])
    print('#{} {}'.format(t+1,''.join(ans)))

