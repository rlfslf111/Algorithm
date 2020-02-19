def perm(k,n,m):
    if k == m:
        for i in range(m):
            print(ans[i],end=' ')
        print()
    for i in range(n):
        if check[i]: continue
        check[i] = True
        ans.append(num_list[i])
        perm(k+1,n,m)
        check[i] = False
        ans.pop()
N, M = map(int,input().split())
num_list = list(range(1,N+1))
ans = list()
check = [False]*N
perm(0,N,M)
