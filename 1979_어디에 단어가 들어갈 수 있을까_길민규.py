import sys
sys.stdin = open('puzzle.txt','r')


def word_insert(puzzle):
    cnt_list = []
    ans_list = []
    for y in range(N):
        cnt = 0
        for x in range(N):
            if puzzle[y][x] == 1:
                cnt += 1
            if cnt == K and puzzle[y][x] == 0:
                cnt_list.append(cnt)
                cnt = 0
            if puzzle[y][x] == 0:
                cnt = 0
        else:
            cnt_list.append(cnt)

    for x in range(N):
        cnt = 0
        for y in range(N):
            if puzzle[y][x] == 1:
                cnt+=1
            if cnt == K and puzzle[y][x] == 0:
                cnt_list.append(cnt)
                cnt = 0
            if puzzle[y][x] == 0:
                cnt = 0
        else:
            cnt_list.append(cnt)

    for i in cnt_list:
        if i == K:
            ans_list.append(i)
    return ans_list



tc = int(input())
for t in range(tc):
    N, K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]

    # #퍼즐 칸 보여주기
    # for i in range(N):
    #     print(puzzle[i])
    # print()

    print('#{} {}'.format(t+1,len(word_insert(puzzle))))


