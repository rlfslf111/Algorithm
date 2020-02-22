def perm(k):
    if k == M:
        print(*ans)
    for i in range(N):
        if check[i]: continue
        check[i] = True
        ans.append(num_list[i])
        perm(k+1)
        check[i] = False
        ans.pop()

N, M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
check = [False] * N
ans = []
perm(0)