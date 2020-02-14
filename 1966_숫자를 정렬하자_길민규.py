def sort_ing(number_list):
    for x in range(len(number_list)-1):
        for y in range(len(number_list)-1-x):
            if number_list[y] > number_list[y+1]:
                number_list[y],number_list[y+1] = number_list[y+1],number_list[y]
    return number_list
tc = int(input())
for t in range(tc):
    number_gesu = int(input())
    number = list(map(int,input().split()))
    sort_ing(number)
    number = [str(_) for _ in number]
    print('#{} {}'.format(t+1,' '.join(number)))