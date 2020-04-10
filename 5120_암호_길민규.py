for t in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    num = list(map(int,input().split()))

    i = 0
    for k in range(K):
        i += M
        if i > len(num):
            i -= len(num)
        elif i == len(num):
            num.append(num[-1]+num[0])
            continue
        num.insert(i,num[i]+num[i-1])

    num.reverse()
    print('#{}'.format(t),*num[0:10])