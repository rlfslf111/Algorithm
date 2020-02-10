def bubble_sort(li):
    for x in range(len(li)):
        for i in range(len(li)-1-x):
            if li[i]>li[i+1]:
                li[i],li[i+1]=li[i+1],li[i]
def building(num):
    test_list=list()
    result=0
    for x in range(2,len(num)-2):
        sum_list=list()
        for i in range(x-2,x+3):
            sum_list.append(num[i])
            bubble_sort(sum_list)
        if num[x]==sum_list[-1]:
            result+=sum_list[-1]-sum_list[-2]
    return result
for x in range(10):
    howmany=int(input())
    height=list(map(int,input().split()))
    print('#{0} {1}'.format(x+1,building(height)))