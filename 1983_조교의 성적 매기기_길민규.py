score = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

tc = int(input())
for t in range(tc):
    stu, K = map(int,input().split())
    score_list = []
    for s in range(stu):
        mid, final, workshop = map(int,input().split())
        mid *= 0.35
        final *= 0.45
        workshop *= 0.2
        score_list.append(mid + final + workshop)
    count = 0
    for x in range(len(score_list)):
        if score_list[K-1] < score_list[x]:
            count += 1
    biyul = stu//10
    idx = count//biyul
    print('#{} {}'.format(t+1,score[idx]))