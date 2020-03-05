import sys
sys.stdin = open('input.txt','r')

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def perm(k,y,x):
    result = ''
    if k == 7:
        for c in range(len(ans)):
            result += ans[c]
        good.add(result)
        return
    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue
        ans.append(num[ny][nx])
        perm(k+1,ny,nx)
        ans.pop()

tc = int(input())
for t in range(1,tc+1):
    num = [list(input().split()) for _ in range(4)]
    ans = []
    good = set()

    for y in range(4):
        for x in range(4):
            perm(0,y,x)

    print('#{} {}'.format(t,len(good)))