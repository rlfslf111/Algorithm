tc = int(input())
for t in range(tc):
    small = input()
    large = input()

    count_list = []
    for x in small:
        count = 0
        for y in large:
            if x == y:
                count += 1
        count_list.append(count)
    print('#{} {}'.format(t+1,max(count_list)))