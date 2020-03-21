for t in range(1,int(input())+1):
    N = int(input())

    route = int(round(N ** (1/3)))
    ans = -1
    for i in range(route+1):
        if i ** 3 == N:
            ans = i
            break
    print('#{} {}'.format(t,ans))