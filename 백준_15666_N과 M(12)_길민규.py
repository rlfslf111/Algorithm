def perm(ans,k):
    if k == M:
        print(*ans)
        return
    else:
        if k == 0:
            for n in num_list:
                perm(ans+[n],k+1)
        else:
            for n in num_list:
                if n >= ans[-1]:
                    perm(ans+[n],k+1)
N, M = map(int,input().split())
num_list = sorted(set(map(int,input().split())))
perm([],0)