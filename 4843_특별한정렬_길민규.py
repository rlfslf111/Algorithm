def sort_ing(number_list):
    for x in range(len(number_list)-1):
        for y in range(len(number_list)-1-x):
            if number_list[y] > number_list[y+1]:
                number_list[y],number_list[y+1] = number_list[y+1],number_list[y]
    return number_list

test_case = int(input())
for t in range(test_case):
    howlong = int(input())
    number_list = list(map(int,input().split()))
    sort_ing(number_list)
    i=len(number_list)-1
    result = []
    for x in range(len(number_list)//2):
       result.append(number_list[i-x])
       result.append(number_list[x])
    result = [str(_) for _ in result]
    real_result = []
    for x in range(10):
        real_result.append(result[x])
    real_real_result = ' '.join(real_result)
    print('#{} {}'.format(t+1,real_real_result))