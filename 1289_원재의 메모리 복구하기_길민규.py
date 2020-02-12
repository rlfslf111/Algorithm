tc = int(input())
for t in range(tc):
    num = list(input())
    num = [int(_) for _ in num]

    board = [[0]*len(num)]

    count = 1
    one = num.index(1)

    for x in range(one,len(num)-1):
        if num[x] == num[x+1]:
            continue
        else:
            count += 1
    print('#{} {}'.format(t+1,count))


