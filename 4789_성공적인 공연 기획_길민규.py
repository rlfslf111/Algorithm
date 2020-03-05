tc = int(input())
for t in range(1,tc+1):
    guest = list(map(int,list(input())))

    cnt = 0
    app = 0
    for i in range(len(guest)):
        if cnt < i:
            app += i - cnt
            cnt += 1
        cnt += guest[i]
    print('#{} {}'.format(t,app))