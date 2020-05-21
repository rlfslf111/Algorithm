def bfs(N,M,cnt):
    visit = set()
    current = set()
    current.add(N)

    while 1:
        if M in current:
            return cnt
        else:
            cnt += 1
            tmp = []
            while current:
                tmp_cur = current.pop()
                tmp.append(tmp_cur)
                visit.add(tmp_cur)
            for i in range(len(tmp)):
                if tmp[i] + 1 not in visit:
                    if tmp[i] + 1 <= 1000000:
                        current.add(tmp[i]+1)
                if tmp[i] - 1 not in visit:
                    if tmp[i] - 1 > 0:
                        current.add(tmp[i]-1)
                if tmp[i] * 2 not in visit:
                    if tmp[i] * 2 <= 1000000:
                        current.add(tmp[i]*2)
                if tmp[i] - 10 not in visit:
                    if tmp[i] - 10 > 0:
                        current.add(tmp[i]-10)

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    ans = bfs(N,M,0)
    print('#{} {}'.format(t,ans))