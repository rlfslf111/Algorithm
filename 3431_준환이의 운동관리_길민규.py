tc = int(input())
for t in range(tc):
    L,U,X = map(int,input().split())

    if L <= X <= U:
        print('#{} {}'.format(t+1,0))
    if X < L:
        print('#{} {}'.format(t+1,L-X))
    if X > U:
        print('#{} {}'.format(t+1,-1))