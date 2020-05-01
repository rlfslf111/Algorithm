def find(idx):
    global ans
    if idx > N:
        return
    find(idx*2)
    ans += tree[idx]
    find(idx*2 + 1)

for t in range(1,11):
    N = int(input())
    tree = ['0'] * (N+1)
    for e in range(N):
        lst = list(input().split())
        tree[int(lst[0])] = lst[1]
    ans = ''
    find(1)
    print('#{}'.format(t),ans)