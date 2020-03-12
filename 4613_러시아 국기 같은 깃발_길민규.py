def perm(k):
    if k == 2:
        ans1 = ans[:]
        result.append(ans1)
        return
    else:
        for i in range(L):
            if check[i]: continue
            check[i] = True
            ans.append(sub_list[i])
            perm(k+1)
            ans.pop()
            for j in range(i+1,L):
                check[j] = False

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    color = [list(input()) for _ in range(N)]

    sub_list = list(range(1,N))
    L = len(sub_list)
    ans = []
    check = [False] * N
    result = []
    perm(0)
    minv = 1231231

    for i in range(len(result)):
        cnt_c = 0
        # white color
        for y in range(0,result[i][0]):
            for w in range(0,M):
                if color[y][w] != 'W':
                    cnt_c += 1

        # blue color
        for y in range(result[i][0],result[i][1]):
            for b in range(0,M):
                if color[y][b] != 'B':
                    cnt_c += 1

        # red color
        for y in range(result[i][1],N):
            for r in range(0,M):
                if color[y][r] != 'R':
                    cnt_c += 1
        minv = min(minv,cnt_c)

    print('#{} {}'.format(t,minv))