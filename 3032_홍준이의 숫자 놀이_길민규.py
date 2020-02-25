def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    ans.append(str(x))
    ans.append(str(y))

tc = int(input())
for t in range(tc):
    A, B = map(int,input().split())
    ans = []
    egcd(A, B)
    print('#{} {}'.format(t+1,' '.join(ans)))