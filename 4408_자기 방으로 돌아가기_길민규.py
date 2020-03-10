for t in range(1,int(input())+1):
    N = int(input())
    aisle = [0] * 200
    for n in range(N):
        move = list(map(int,input().split()))
        move.sort()

        for i in range((move[0]-1)//2,(move[1]+1)//2):
            aisle[i] += 1

    print('#{} {}'.format(t,max(aisle)))