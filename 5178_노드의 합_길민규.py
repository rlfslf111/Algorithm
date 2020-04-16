for t in range(1,int(input())+1):
    N, M, L = map(int,input().split())
    num = [0 for _ in range(N+1)]

    for m in range(M):
        y, x = map(int,input().split())
        num[y] = x

    for i in range(len(num)-1,0,-1):
        if i*2 < len(num) and i*2 + 1 == len(num):
            num[i] = num[i*2]
        elif i*2 < len(num) and i*2 + 1 < len(num):
            num[i] = num[i*2] + num[i*2 + 1]

    print('#{} {}'.format(t,num[L]))

