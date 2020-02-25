T = int(input())
for t in range(T):
    N, K = map(int,input().split())
    num_list = list(map(int,input().split()))

    ans = []
    for i in range(1<<N):
        sum = 0
        for j in range(N):
            if i & (1 << j):
                sum += num_list[j]
        ans.append(sum)
    print('#{} {}'.format(t+1,ans.count(K)))