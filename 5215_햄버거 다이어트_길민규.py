def combi(k,sum,sco):
    if sum < L:
        maxv[0] = max(maxv[0],sco)
    for i in range(N):
        if not check[i]:
            check[i] = True
            combi(k+1,sum+sk[i][1],sco+sk[i][0])
            for j in range(i+1,N):
                check[j] = False

tc = int(input())
for t in range(tc):
    N, L = map(int,input().split())
    sk = []
    for n in range(N):
        score, kal = map(int,input().split())
        sk.append([score,kal])

    check = [False] * len(sk)
    maxv = [0]
    combi(0,0,0)
    print('#{} {}'.format(t+1,maxv[0]))