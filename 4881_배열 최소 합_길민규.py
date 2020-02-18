def permutation(k,n,y):
    global min_res
    if sum(ans) > min_res:
        return
    if k == n:
        if sum(ans) < min_res:
            min_res = sum(ans)
    for i in range(n):
        if check[i]: continue
        check[i] = True
        ans.append(board[y][i])
        permutation(k+1,n,y+1)
        check[i] = False
        ans.pop()

tc = int(input())
for t in range(tc):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    min_res = 10000
    check = [False] * N
    ans = []
    permutation(0,N,0)
    print('#{} {}'.format(t+1,min_res))