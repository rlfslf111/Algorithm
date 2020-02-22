tc = int(input())
for t in range(tc):
    N = int(input())
    ans = []
    for x in range(N):
        ans.append('1/{}'.format(N))
    print('#{} {}'.format(t+1,' '.join(ans)))