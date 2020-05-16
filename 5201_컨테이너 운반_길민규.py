for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)

    result = 0
    for i in range(len(truck)):
        for j in range(len(container)):
            if container[j] != 0 and truck[i] >= container[j]:
                result += container[j]
                container[j] = 0
                break

    print('#{} {}'.format(t,result))
