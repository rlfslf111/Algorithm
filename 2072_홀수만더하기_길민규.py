test_case = int(input())
for x in range(test_case):
    su = list(map(int,input().split()))
    sum=0
    for i in su:
        if i%2!=0:
            sum+=i
    print('#{} {}'.format(x+1,sum))