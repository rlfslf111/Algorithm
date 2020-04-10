for t in range(1,int(input())+1):
    N, M, L = map(int,input().split())
    num_list = list(map(int,input().split()))

    for m in range(M):
        order = list(input().split())
        if order[0] == 'I':
            num_list.insert(int(order[1]),int(order[2]))
        elif order[0] == 'D':
            del num_list[int(order[1])]
        elif order[0] == 'C':
            num_list[int(order[1])] = int(order[2])

    if len(num_list) >= L+1:
        print('#{} {}'.format(t,num_list[L]))
    else:
        print('#{} {}'.format(t,-1))

