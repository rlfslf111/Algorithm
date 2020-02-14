tc = int(input())
for t in range(tc):
    N = int(input())
    num_list = [input().split() for _ in range(N)]

    result = []

    for x in range(N):
        one_one = ''
        for y in range(N-1,-1,-1):
            one_one += num_list[y][x]
        result.append(one_one)

    for y in range(N-1,-1,-1):
        one_two = ''
        for x in range(N-1,-1,-1):
            one_two += num_list[y][x]
        result.append(one_two)

    for x in range(N-1,-1,-1):
        one_three = ''
        for y in range(N):
            one_three += num_list[y][x]
        result.append(one_three)

    board = [[0]*3 for _ in range(N)]
    i=0
    for x in range(3):
        for y in range(N):
            board[y][x] = result[i]
            i+=1
    print('#{}'.format(t+1))
    for i in range(N):
        print(' '.join(map(str,board[i])))