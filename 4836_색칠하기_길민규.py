test_case = int(input())
for t in range(test_case):
    color_gesu = int(input())
    red_list = []
    blue_list = []
    for i in range(color_gesu):
        y1,x1,y2,x2,color = map(int,input().split())
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                if color==1:
                    red_list.append((y,x))
                elif color==2:
                    blue_list.append((y,x))
    result_list = []
    if len(red_list)>len(blue_list):
        for blue in blue_list:
            if blue in red_list:
                result_list.append(blue)
    if len(blue_list)>len(red_list):
        for red in red_list:
            if red in blue_list:
                result_list.append(red)
    print('#{} {}'.format(t+1,len(result_list)))