def cost(k,sum):
    if sum > ans[0]:
        return
    if k == N:
        ans[0] = min(ans[0],sum)
        return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            cost(k+1,sum+board[k][i])
            check[i] = 0

for t in range(1,int(input())+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    check = [0] * N
    ans = [1231231]
    cost(0,0)
    print('#{} {}'.format(t,ans[0]))