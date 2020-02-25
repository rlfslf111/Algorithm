tc = int(input())
initial = [11,11,11]
for t in range(tc):
    D, H, M = map(int,input().split())

    ans = 0
    if D < initial[0] or (D <= initial[0] and H < initial[1]) or (D <= initial[0] and H <= initial[1] and M < initial[2]):
        print('#{} {}'.format(t+1,-1))
    else:
        ans += ((D-initial[0])*24*60) + ((H-initial[1])*60) + (M-initial[2])
        print('#{} {}'.format(t+1,ans))
