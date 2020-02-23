tc = int(input())
for t in range(tc):
    N, M = map(int,input().split())
    twin = N-M
    uni = M - twin
    print('#{} {} {}'.format(t+1,uni,twin))