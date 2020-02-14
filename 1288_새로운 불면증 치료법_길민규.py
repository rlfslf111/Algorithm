def insomnia(N):
    number_count = [0]*10
    su =1
    sheep = 1
    while True:
        sheep = N*su
        sheep = list(str(sheep))
        sheep = [int(_) for _ in sheep]
        for x in range(len(sheep)):
            number_count[sheep[x]]+=1
        sheep = [str(_) for _ in sheep]
        N_int = ''
        for x in sheep:
            N_int += x
        sheep = int(N_int)
        su+=1
        if 0 not in number_count:
            return sheep

test_case = int(input())
for x in range(test_case):
    N = int(input())
    print('#{} {}'.format(x+1,insomnia(N)))