tc = int(input())
for t in range(tc):
    N,M = map(int,input().split())
    number = [list(map(int,input().split())) for _ in range(N)]
    sum_list = []
    for y in range(N-M+1):
        for x in range(N-M+1):
            sum = 0
            #number[y][x]가 각 인자의 지점
            for y1 in range(M):
                for x1 in range(M):
                    sum += number[y+y1][x+x1]
                    sum_list.append(sum)
    print('#{} {}'.format(t+1,max(sum_list)))