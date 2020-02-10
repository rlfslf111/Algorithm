def snail_number(number):
    direction_list = [(0,1),(1,0),(0,-1),(-1,0)]
    direction_index = 0
    num=0
    current_y = 0
    current_x = -1
    number_list = [[-1]*number for _ in range(number)]
    while num < number**2:
        move = direction_list[direction_index]
        temp_y = current_y + move[0]
        temp_x = current_x + move[1]

        if temp_y < 0 or temp_y >= number or temp_x < 0 or temp_x >= number or number_list[temp_y][temp_x] != -1:
            direction_index+=1
            if direction_index == 4:
                direction_index = 0
        else:
            num+=1
            current_y,current_x = temp_y,temp_x
            number_list[current_y][current_x] = num
    return number_list

test_case = int(input())
for x in range(test_case):
    number = int(input())
    print('#{}'.format(x+1))
    for i in snail_number(number):
        print(' '.join(map(str,i)))