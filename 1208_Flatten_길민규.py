# import sys
# sys.stdin = open('input.txt','r')
#1208 dump문제
def bubble_sort(number):
    for x in range(len(number)-1):
        for i in range(len(number)-1-x):
            if number[i]>number[i+1]:
                number[i],number[i+1]=number[i+1],number[i]

for x in range(10):
    dump=int(input())
    dump_list=list(map(int,input().split()))
    bubble_sort(dump_list)
    for y in range(dump): #dump 횟수
        dump_list[-1]-=1
        dump_list[0]+=1
        bubble_sort(dump_list)
    result = dump_list[-1] - dump_list[0]
    print('#{} {}'.format(x+1,result))