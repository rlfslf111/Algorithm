def perm(k,idx):
    if k == M:
        print(*ans)
    same = 0
    for i in range(idx,N):
        if not check[i] and same != num_list[i]:
            check[i] = True
            ans.append(num_list[i])
            same = num_list[i]
            perm(k+1,i+1)
            ans.pop()
            check[i] = False

N, M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
check = [False] * N
ans = []
perm(0,0)