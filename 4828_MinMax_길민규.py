def minmax(num):
    for x in range(len(num)-1):
        for i in range(len(num)-1-x):
            if num[i]>num[i+1]:
                num[i],num[i+1]=num[i+1],num[i]
                result=num[-1]-num[0]
    return result

test_case=int(input())
for x in range(test_case):
    howmany=int(input())
    arr=list(map(int,input().split()))
    print('#{0} {1}'.format(x+1,minmax(arr)))