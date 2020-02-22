def perm(k):
    if k == M:
        print(*ans)
        return
    for i in range(N):
        if not check[i]:
            ans.append(num_list[i])
            perm(k+1)
            check[i] = True
            ans.pop()
            for j in range(i+1,N):
                check[j] = False

N, M = map(int,input().split())
num_list = list(map(int,input().split()))
check = [False] * N
ans = []
num_list.sort()
perm(0)