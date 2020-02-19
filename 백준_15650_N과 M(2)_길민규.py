def permutation(count):
    if count == M:
        print(*ans)
    for i in range(N):
        if check[i]: continue
        check[i] = True
        ans.append(num_list[i])

        permutation(count+1)

        ans.pop()
        # 이 부분이 순열하고의 차이점
        # 큰 트리에서 전에 봤던 것만 닫아주면 된다.
        for j in range(i+1,N):
            check[j] = False

N, M =map(int,input().split())
num_list = list(range(1,N+1))
check = [False]*N
ans = []
permutation(0)