test_case = int(input())
for x in range(test_case):
    su = list(map(int,input().split()))
    sum=0
    for i in su:
        sum+=i
    avg=sum/len(su)
    avg_round=round(avg)
    print('#{} {}'.format(x+1,avg_round))