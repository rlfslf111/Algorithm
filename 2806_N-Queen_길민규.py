def perm(k):
    global cnt
    if k == N:
        cnt+=1
    for i in range(N):
        if check[i]: continue
        flag[0] = False
        #깊이 만큼 반복문을 수행해라.
        for j in range(k):
            if abs(k-j) == abs(i-ans[j]):
                flag[0] = True
                break
        if flag[0]:
            continue
        check[i] = True
        ans.append(i)
        perm(k+1)
        ans.pop()
        check[i] = False

tc = int(input())
for t in range(tc):
    N = int(input())
    check = [False] * N
    ans = []
    flag = [False]
    cnt = 0
    perm(0)
    print('#{} {}'.format(t+1,cnt))


