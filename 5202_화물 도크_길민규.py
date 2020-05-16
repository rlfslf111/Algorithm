def find(k,pos):
    if k == len(time):
        ans[0] = max(len(pos),ans[0])
        return

    else:
        if len(time) - k + len(pos) <= ans[0]:
            return
        if pos[-1][1] <= time[k][0]:
            pos.append(time[k])
            find(k+1,pos)
            pos.pop()

        find(k+1,pos)

for t in range(1,int(input())+1):
    N = int(input())
    time = set()
    for _ in range(N):
        time.add(tuple(map(int,input().split())))

    time = sorted(time, key=lambda x : (x[0],x[1]))

    pos = [(0,0),]
    ans = [0]
    find(0,pos)
    print('#{} {}'.format(t,ans[0]-1))