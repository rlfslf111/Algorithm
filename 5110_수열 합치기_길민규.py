for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    total = []
    for _ in range(M):
        total.append(list(map(int,input().split())))
    ans = total[0]
    for i in range(1,M):
        temp = total[i][0]
        for j in range(len(ans)):
            if temp < ans[j]:
                ans[j:j] = total[i]
                break
        else:
            ans += total[i]
    ans = ans[-10:]
    ans.reverse()
    print('#{}'.format(t),*ans)