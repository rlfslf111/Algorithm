year = {
    0:0,
    1:31,
    2:29,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
week = [0,1,2,3,4,5,6] #월화수목금토일
tc = int(input())
for t in range(tc):
    m, d = map(int,input().split())

    cnt = 0
    for x in range(m):
        cnt += year[x]
    cnt += d

    if cnt % 7 == 1:
        print('#{} {}'.format(t+1,4))
    elif cnt % 7 == 2:
        print('#{} {}'.format(t+1,5))
    elif cnt % 7 == 3:
        print('#{} {}'.format(t+1,6))
    elif cnt % 7 == 4:
        print('#{} {}'.format(t+1,0))
    elif cnt % 7 == 5:
        print('#{} {}'.format(t+1,1))
    elif cnt % 7 == 6:
        print('#{} {}'.format(t+1,2))
    elif cnt % 7 == 0:
        print('#{} {}'.format(t+1,3))
