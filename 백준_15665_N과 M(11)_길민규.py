def perm(k):
    if k == M:
        print(*ans)
        return
    same = 0
    for i in range(N):
        if same != num_list[i]:
            ans.append(num_list[i])
            same = num_list[i]
            perm(k+1)
            ans.pop()

N, M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
# check = [False] * N
ans = []
perm(0)