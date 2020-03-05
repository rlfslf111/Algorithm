import sys
sys.stdin = open('input.txt','r')

tc = int(input())
for t in range(1,tc+1):
    N = int(input())
    day = []
    for n in range(N):
        day.append(int(input()))

    # 1일과의 차이를 받는다.
    sub_day = []
    for i in range(1,len(day)):
        sub_day.append(day[i]-1)

    k = 0
    visit = [0] * len(sub_day)
    s = []
    while k != len(sub_day):
        if visit[k] == 0:
            s.append(sub_day[k])
        for y in range(len(sub_day)):
            if sub_day[y] % s[-1] == 0:
                visit[y] = 1
        k += 1
    print('#{} {}'.format(t,len(s)))
