tc = int(input())
for t in range(tc):
    num = list(input())

    if int(num[-1]) % 2 == 0 or int(num[-1]) == 0:
        print('#{} {}'.format(t+1,'Even'))
    else:
        print('#{} {}'.format(t+1,'Odd'))