for t in range(1,int(input())+1):
    N, M, L = map(int,input().split())
    num_list = list(map(int,input().split()))
    for m in range(M):
        index, num = map(int,input().split())
        num_list.insert(index,num)

    print('#{} {}'.format(t,num_list[L]))