tc = int(input())
for t in range(tc):
    N, K = map(int,input().split())
    score = list(map(int,input().split()))
    score.sort(reverse=True)

    sum = 0
    for x in range(K):
        sum += score[x]
    print('#{} {}'.format(t+1,sum))