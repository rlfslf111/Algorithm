test_case=int(input())
for i in range(test_case):
    test_case_number = int(input())
    score = list(map(int,input().split()))
    count_list = [0]*1000
    for x in range(len(count_list)):
        count_list[score[x]]+=1
    max_index = 0
    max_num = 0
    for x in range(len(count_list)-1,-1,-1):
        if count_list[x]>max_index:
            max_index = count_list[x]
            max_num = x
    print('#{} {}'.format(i+1,max_num))