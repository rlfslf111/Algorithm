dy = [0,1,0,-1]
dx = [1,0,-1,0]

def snail(number):
    current_y = 0
    current_x = -1
    start_num = 0
    dir = 0
    num_list = [[-1]*number for i in range(number)]

    while start_num < number**2:
        temp_y = current_y + dy[dir]
        temp_x = current_x + dx[dir]
        if temp_y < 0 or temp_y >= number or temp_x < 0 or temp_x >= number or num_list[temp_y][temp_x] != -1:
            dir += 1
            if dir >= 4:
                dir = 0
        else:
            current_y = temp_y
            current_x = temp_x
            start_num += 1
            num_list[current_y][current_x] = start_num
    return num_list

case = int(input())
for x in range(case):
    num = int(input())
    print('#{}'.format(x+1))
    result = snail(num)
    for i in range(len(result)):
        print(' '.join(map(str,result[i])))

