for t in range(1,int(input())+1):
    N = int(input())
    ls = list(map(int,input().split()))

    ls.sort()
    print('#{} {}'.format(t,ls[N//2]))