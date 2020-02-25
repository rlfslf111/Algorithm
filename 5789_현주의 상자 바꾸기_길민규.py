tc = int(input())
for t in range(tc):
    N, Q = map(int,input().split())
    box = [str(0)] * N

    for i in range(1,Q+1):
        L, R = map(int,input().split())

        for x in range(L-1,R):
            box[x] = str(i)
    print('#{} {}'.format(t+1,' '.join(box)))



