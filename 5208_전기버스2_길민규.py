def go(charge,straight,cnt):
    if cnt >= ans[0]:
        return
    if charge >= input_[0]:
        ans[0] = min(ans[0],cnt)
        return
    else:
        go(charge+1,input_[charge] - 1, cnt + 1)
        if straight:
            go(charge + 1, straight - 1, cnt)

for t in range(1,int(input())+1):
    input_ = list(map(int,input().split()))
    ans = [1231231]
    go(2,input_[1] - 1,0)
    print('#{} {}'.format(t,ans[0]))
