tc = int(input())
for t in range(tc):
    h1,m1,h2,m2 = map(int,input().split())
    sum_h = h1+h2
    sum_m = m1+m2
    if sum_h > 12:
        sum_h = sum_h % 12
    if sum_m > 60:
        sum_m = sum_m % 60
        sum_h += 1
    print('#{} {} {}'.format(t+1,sum_h,sum_m))