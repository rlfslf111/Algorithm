def permutation(count):
    if count == M:
        print(*ans)
    for i in range(N):
        if check[i]: continue
        check[i] = True
        ans.append(num_list[i])

        permutation(count+1)

        ans.pop()
        for j in range(i+1,N):
            check[j] = False

N, M =map(int,input().split())
num_list = list(range(1,N+1))
check = [False]*N
ans = []
permutation(0)