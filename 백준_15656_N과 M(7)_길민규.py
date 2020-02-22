def perm(k):
    if k == M:
        print(*ans)
        return
    for i in range(N):
        ans.append(num_list[i])
        perm(k+1)
        ans.pop()

N, M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
ans = []
perm(0)