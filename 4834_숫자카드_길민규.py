test_case=int(input())
for x in range(test_case):
    howlong=int(input())
    number = input()
    number = [int(_) for _ in number]
    count_list = [0 for i in range(10)]
    for y in range(howlong):
        count_list[number[y]]+=1
    max_index=0
    max_num=0
    for y in range(len(count_list)-1,-1,-1):
        if count_list[y]>max_index:
            max_index=count_list[y]
            max_num=y
    print('#{} {} {}'.format(x+1,max_num,max_index))