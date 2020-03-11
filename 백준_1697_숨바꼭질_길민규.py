def bfs(N,K,cnt):
    visit = set()
    location = set()
    location.add(N)

    while 1:
        if K in location:
            return cnt
        else:
            cnt += 1
            tmp = []
            while location:
                tmp_loc = location.pop()
                tmp.append(tmp_loc)
                visit.add(tmp_loc)
            for i in range(len(tmp)):
                if tmp[i] + 1 not in visit:
                    if tmp[i]+1 <= 100000:
                        location.add(tmp[i]+1)
                if tmp[i] - 1 not in visit:
                    if tmp[i]-1 >= 0:
                        location.add(tmp[i]-1)
                if tmp[i]*2 not in visit:
                    if tmp[i]*2 <= 100000:
                        location.add(tmp[i]*2)

N, K = map(int,input().split())
cnt = 0
cnt = bfs(N,K,cnt)
print(cnt)
