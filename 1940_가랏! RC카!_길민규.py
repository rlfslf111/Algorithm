test_case = int(input())
for x in range(test_case):
    command_count = int(input())
    base_meter = 0
    acceleration = 0
    for y in range(command_count):
        command = list(map(int,input().split()))
        if command[0]==1:
            acceleration+=command[1]
            base_meter+=acceleration
        if command[0]==0:
            base_meter+=acceleration
        if command[0]==2:
            acceleration-=command[1]
            if acceleration < 1:
                acceleration = 0
            base_meter+=acceleration
    print('#{} {}'.format(x+1,base_meter))