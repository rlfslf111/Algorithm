def meter(ans):
    d = 0
    for y in range(N+1):
        for x in range(N+1):
            if road[y][x] == 1:
                house = 1231231

                #치킨 집 위치
                for i in range(len(ans)):
                    chiy,chix = ans[i][0],ans[i][1]
                    house = min(house, abs(y - chiy) + abs(x - chix))
                d += house
    minv[0] = min(d,minv[0])

def perm(k):
    if k == M:
        meter(ans)
        return
    else:
        for i in range(len(chicken)):
            if not check[i]:
                ans.append(chicken[i])
                check[i] = True
                perm(k+1)
                for j in range(i+1,len(chicken)):
                    check[j] = False
                ans.pop()

N, M = map(int,input().split())

road = [[0] * (N+1)]
for n in range(N):
    row = [0] + list(map(int, input().split()))
    road.append(row)

minv = [1231231]

chicken = []
for y in range(N+1):
    for x in range(N+1):
        if road[y][x] == 2:
            chicken.append((y,x))

ans = []
check = [False] * len(chicken)
perm(0)
print(minv[0])