for t in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    time = list(map(int,input().split()))
    time.sort()
    # 0초에 손님이 온다면?
    if time[0] == 0:
        print('#{} Impossible'.format(t))
    else:
        make = [0]*(max(time)+1)
        for i in range(M,len(make),M):
            make[i] = K

        flag = True
        come = 1
        bread = 0
        idx = 0
        while come != max(time)+1:
            bread += make[come]
            if come == time[idx]:
                bread -= 1
                idx += 1
                if bread < 0:
                    flag = False
                    break
            come += 1

        if flag:
            print('#{} Possible'.format(t))
        else:
            print('#{} Impossible'.format(t))