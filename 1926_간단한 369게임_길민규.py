N = int(input())
number_list = list(map(str,range(1,N+1)))

for x in range(len(number_list)):
    count = 0
    for i in range(len(number_list[x])):
        if number_list[x][i] == '3' or number_list[x][i] == '6' or number_list[x][i] == '9':
            count += 1
    if count == 1:
        number_list[x] = '-'
    elif count == 2:
        number_list[x] = '--'
print(' '.join(number_list))
