for t in range(1,int(input())+1):
    W, H, N = map(int,input().split())
    road = []
    for n in range(N):
        x, y = map(int,input().split())
        road.append([y,x])

    cnt = 0
    for i in range(N-1):
        # 둘 다 증가 혹은 둘 다 감소할 때는 y,x 차 중 큰 값만 더 해준다.
        pre_y, next_y = road[i][0], road[i+1][0]
        pre_x, next_x = road[i][1], road[i+1][1]
        if (pre_y < next_y and pre_x < next_x) or (pre_y > next_y and pre_x > next_x):
            my, mx = abs(next_y-pre_y), abs(next_x-pre_x)
            if my >= mx:
                cnt += my
            else:
                cnt += mx
        # 한쪽만 증가 혹은 감소를 할 경우는 각각의 차를 더해준다.
        else:
            my, mx = abs(next_y-pre_y), abs(next_x-pre_x)
            cnt += my + mx

    print('#{} {}'.format(t,cnt))




