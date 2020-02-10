tc=int(input())
for t in range(tc):
    number = int(input())
    pascal = [0] * number
    for x in range(number):
        pascal[x] = [0] * (x + 1)
    for y in range(number):
        for x in range(number):
            pascal[y][0] = 1
            pascal[y][-1] = 1

    for y in range(1,number):
        for x in range(1,len(pascal[y])):
            if pascal[y][x] == 0:
                pascal[y][x] = pascal[y-1][x-1] + pascal[y-1][x]

    print('#{}'.format(t+1))
    for x in range(number):
        print(' '.join(map(str,pascal[x])))
