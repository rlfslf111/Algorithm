for t in range(10):
    gesu = input()
    number_list = [list(map(int,input().split())) for _ in range(100)]

    x_sum_list = []
    sum_x = 0
    for i in range(100):
        for j in range(100):
            sum_x += number_list[i][j]
        x_sum_list.append(sum_x)
        sum_x=0

    y_sum_list = []
    sum_y = 0
    for i in range(100):
        for j in range(100):
            sum_y += number_list[j][i]
        y_sum_list.append(sum_y)
        sum_y=0

    cross_sum_list=[]
    sum_cross = 0
    for i in range(100):
        for j in range(100):
            if i==j:
                sum_cross += number_list[i][j]
    cross_sum_list.append(sum_cross)

    revers_cross_sum_list = []
    sum_reverse_cross = 0
    for i in range(100):
        for j in range(100):
            if i==100-i:
                sum_reverse_cross += number_list[i][j]
    revers_cross_sum_list.append(sum_reverse_cross)

    bin_list = []
    for x in x_sum_list:
        bin_list.append(x)
    for x in y_sum_list:
        bin_list.append(x)
    for x in cross_sum_list:
        bin_list.append(x)
    for x in revers_cross_sum_list:
        bin_list.append(x)
    print('#{} {}'.format(t+1,max(bin_list)))