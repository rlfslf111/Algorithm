tc = int(input())
for t in range(tc):
    N, M = map(int,input().split())
    submit = list(map(int,input().split()))
    student = list(range(1,N+1))

    ans = []
    for x in range(N):
        if student[x] not in submit:
            ans.append(str(student[x]))
    print('#{} {}'.format(t+1,' '.join(ans)))