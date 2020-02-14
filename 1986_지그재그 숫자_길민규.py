tc = int(input())
for t in range(tc):
    sum = 0
    num = int(input())
    for x in range(1,num+1):
        if x%2 != 0:
            sum+=x
        if x%2 == 0:
            sum-=x
    print('#{} {}'.format(t+1,sum))