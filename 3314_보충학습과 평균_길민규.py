tc = int(input())
for t in range(tc):
    score = list(map(int,input().split()))

    for x in range(len(score)):
        if score[x] < 40:
            score[x] = 40

    sum = 0
    for x in range(len(score)):
        sum += score[x]
    avg = sum//len(score)
    print('#{} {}'.format(t+1,avg))