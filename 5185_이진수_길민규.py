for t in range(1,int(input())+1):
    N, num = input().split()
    num = list(num)
    ls = [0 for _ in range(4)]
    print('#{}'.format(t),end=' ')
    for i in range(len(num)):
        hexa = int(num[i],16)
        result = format(hexa,'b')

        if len(result) == 4:
            for j in range(len(result)):
                ls[j] += int(result[j])
            for j in range(len(ls)):
                print(ls[j],end='')
            ls = [0 for _ in range(4)]
        elif len(result) == 3:
            for j in range(len(result)):
                ls[j+1] += int(result[j])
            for j in range(len(ls)):
                print(ls[j], end='')
            ls = [0 for _ in range(4)]
        if len(result) == 2:
            for j in range(len(result)):
                ls[j+2] += int(result[j])
            for j in range(len(ls)):
                print(ls[j],end='')
            ls = [0 for _ in range(4)]
        elif len(result) == 1:
            for j in range(len(result)):
                ls[j+3] += int(result[j])
            for j in range(len(ls)):
                print(ls[j],end='')
            ls = [0 for _ in range(4)]
    print()