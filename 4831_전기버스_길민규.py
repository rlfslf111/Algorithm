import sys
sys.stdin = open('sample_input.txt','r')

test_case = int(input())
for tc in range(1, test_case+1):
    charge_K,station_N,install_M = map(int,input().split())
    station = list(map(int, input().split()))
    station_list = [0] * (station_N+1)
    for i in range(len(station)):
        station_list[station[i]] += 1
    start = 0
    end = charge_K
    cnt = 0
    while True:
        zero = 0
        for i in range(start+1, end+1):
            if station_list[i] == 1:
                start = i
            else:
                zero += 1
        if zero == charge_K:
            cnt = 0
            break
        cnt += 1
        end = start + charge_K
        if end >= station_N:
            break
    print('#{} {}'.format(tc, cnt))