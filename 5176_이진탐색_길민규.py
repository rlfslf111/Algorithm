def find(idx):
    global N
    if idx > N:
        return
    find(idx*2)
    ans[idx] = cnt[0]
    cnt[0] += 1
    find(idx*2 + 1)

for t in range(1,int(input())+1):
    N = int(input())
    ans = [0] * (N+1)
    cnt = [1]
    find(1)
    print('#{} {} {}'.format(t,ans[1],ans[N//2]))