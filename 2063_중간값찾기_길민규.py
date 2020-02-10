def bubble_sort(number_list):
    for x in range(len(number_list)-1):
        for y in range(len(number_list)-1-x):
            if number_list[y]>number_list[y+1]:
                number_list[y],number_list[y+1]=number_list[y+1],number_list[y]

    return number_list[len(number_list)//2]
howmany=int(input())
number_list = list(map(int,input().split()))
print(bubble_sort(number_list))