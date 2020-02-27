tc = int(input())
for t in range(tc):
    N = int(input())
    station = [0] * 5001

    #A~B까지 운행하는 만큼 카운트
    for n in range(N):
        A, B = map(int,input().split())
        for i in range(A,B+1):
            station[i] += 1

    #원하는 정류소 확인
    P = int(input())
    ans = []
    for p in range(P):
        C = int(input())
        ans.append(str(station[C]))
    print('#{} {}'.format(t+1,' '.join(ans)))