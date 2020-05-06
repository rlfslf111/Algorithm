from itertools import permutations

for t in range(1,int(input())+1):
    N = int(input())
    office = [list(map(int,input().split())) for _ in range(N)]
    minv = 1231231

    for k in permutations(range(2,N+1),N-1):
        line = [1]
        for i in range(len(k)):
            line.append(k[i])
        line.append(1)


        ans = 0
        for x in range(len(line)-1):
            ans += office[line[x]-1][line[x+1]-1]
        if minv > ans:
            minv = ans

    print('#{} {}'.format(t,minv))