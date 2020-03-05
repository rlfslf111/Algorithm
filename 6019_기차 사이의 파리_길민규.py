tc = int(input())
for t in range(1,tc+1):
    D, A, B, F = map(float,input().split())
    velocity = A+B
    time = D/velocity
    ans = F * time
    print('#{} {:0.6f}'.format(t,ans))
