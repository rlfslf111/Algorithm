def sort_ing(num):
    for x in range(len(num)):
        for i in range(len(num)-1-x):
            if num[i] > num[i+1]:
                num[i],num[i+1]=num[i+1],num[i]
    return num


tc = int(input())
for t in range(tc):
    num = list(map(str,input().split()))
    num = [int(_) for _ in num]
    num = sort_ing(num)
    sum = 0
    for x in range(1,len(num)-1):
        sum += num[x]
    result = round(sum/(len(num)-2))
    print('#{} {}'.format(t+1,result))