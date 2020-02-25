def game(k):
    if k == 3:
        sum = 0
        for x in range(len(ans)):
            sum += ans[x]
        result.append(sum)
    for i in range(N):
        if not check[i]:
            check[i] = True
            ans.append(num_list[i])
            game(k+1)
            ans.pop()
            for j in range(i+1,N):
                check[j] = False

tc = int(input())
for t in range(tc):
    num_list = list(map(int,input().split()))
    N = len(num_list)
    check = [False] * N
    ans = []
    result = []
    game(0)
    result = set(result)
    result = list(result)
    result.sort(reverse=True)
    print('#{} {}'.format(t+1,result[4]))


