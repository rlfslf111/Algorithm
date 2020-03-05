import sys
sys.stdin = open('input.txt','r')

def div(a):
    return int(a)/100

def success(k,z):
    if z <= result[0]:
        return
    if k == N:
        result[0] = max(result[0],z)
        return
    else:
        for i in range(N):
            if not check[i]:
                check[i] = True
                success(k+1, per[k][i] * z)
                check[i] = False

tc = int(input())
for t in range(1,tc+1):
    N = int(input())
    per = [list(map(div,input().split())) for _ in range(N)]
    check = [False] * N

    result = [0]
    success(0,100)

    print('#{} {:.6f}'.format(t,result[0]))
