def mono_increment(number_list):
    multi_list = list()
    for x in range(0,len(number_list)-1):
        for y in range(x+1,len(number_list)):
            multi = number_list[x]*number_list[y]
            multi_list.append(str(multi))
    # 리스트에서 단조 증가 함수 일때 각 자리의 곱을 구함
    # 구한 곱의 수가 단조 증가 함수 일때 가장 큰 수 뽑기 ㄱㄱ
    result_list = []
    for x in multi_list:
        for y in range(len(x)-1):
            if x[y] > x[y+1]:
                break
        else:
            result_list.append(x)
    result_list = [int(_) for _ in result_list]
    if len(result_list) == 0:
        return -1
    return max(result_list)


test_case = int(input())
for t in range(test_case):
    number_gesu = int(input())
    number_list = list(map(int,input().split()))
    print('#{} {}'.format(t+1,mono_increment(number_list)))