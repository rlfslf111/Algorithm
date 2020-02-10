def gugan(num,gesu):
    gu_list=list()
    result=0
    for x in range(0,len(num)-gesu+1):
        for i in range(x,x+gesu):
            result+=num[i]
        gu_list.append(result)
        result=0
    for x in range(len(gu_list)-1):
        for y in range(len(gu_list)-x-1):
            if gu_list[y]>gu_list[y+1]:
                gu_list[y],gu_list[y+1]=gu_list[y+1],gu_list[y]
    exell=gu_list[-1]-gu_list[0]
    return exell
test_case=int(input())
for x in range(test_case):
    count,howmany=map(int,input().split())
    su=list(map(int,input().split()))
    print('#{0} {1}'.format(x+1,gugan(su,howmany)))