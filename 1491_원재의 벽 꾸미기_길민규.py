for t in range(1,int(input())+1):
    N, A, B = map(int,input().split())
    C = 0
    minv = 123123123123

    for i in range(1,N+1):
        if i**2 > N:
            break
        C = N//i
        ans = A*abs(i-C) + B*abs(N-i*C)
        minv = min(minv,ans)
        C = i
        ans = A*abs(i-C) + B*abs(N-i*C)
        minv = min(minv,ans)

    print('#{} {}'.format(t,minv))