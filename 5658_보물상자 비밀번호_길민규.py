import sys
sys.stdin = open('password.txt','r')

tc = int(input())
for t in range(1,tc+1):
    N, K = map(int,input().split())
    ox = list(input())

    result = set()
    i = 0
    soju = []
    while i != N//4+1:
        for k in range(len(ox)-N//4):
            ans = ''
            for j in range(k,k+N//4):
                ans += ox[j]
            result.add(ans)

        soju.append(ox[-1])
        del ox[-1]
        ox.insert(0,soju[0])
        del soju[0]
        i+=1

    answser = []
    for x in result:
        answser.append(int(x,16))
    answser.sort(reverse=True)
    print('#{} {}'.format(t,answser[K-1]))