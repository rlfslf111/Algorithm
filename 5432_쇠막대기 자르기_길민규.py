for t in range(1,int(input())+1):
    bracket = list(input())
    laser = [bracket[0]]
    laser_num = 0
    s = []
    stick = []
    stick_num = 0

    for i in range(1,len(bracket)):
        if laser[-1] == '(' and bracket[i] == ')':
            laser.append('L')
        else:
            laser.append(bracket[i])

    for i in range(len(laser)):
        if laser[i] == '(':
            laser_num += 1
        elif laser[i] == ')':
            laser_num -= 1
        elif laser[i] == 'L' and i - 1 >= 0:
            laser_num -= 1
            laser[i-1] = 'L'
            s.append(laser_num)

    for i in range(len(laser)):
        if not stick and laser[i] == '(':
            stick.append(laser[i])
        elif laser[i] == '(':
            stick.append(laser[i])
        elif laser[i] == ')':
            stick.pop()
            stick_num += 1

    ans = sum(s) + stick_num
    print('#{} {}'.format(t,ans))

