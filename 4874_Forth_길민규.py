import sys
sys.stdin = open('calcul.txt','r')

def verify(calcul):
    num = []
    operator = []
    for x in calcul:
        if x.isnumeric():
            num.append(int(x))
        else:
            operator.append(x)
    if len(num) < len(operator):
        return False
    return True

tc = int(input())
for t in range(tc):
    calcul = list(input().split())

    num = []
    cal_stack = []
    if verify(calcul):
        for x in calcul:
            if x.isnumeric():
                num.append(int(x))
            if x == '+' and len(num) > 1:
                if len(num) < 2:
                    print('#{} {}'.format(t+1,'error'))
                    break
                cal_stack.append(num.pop())
                cal_stack.append(num.pop())
                num.append(cal_stack[-1]+cal_stack[0])
                cal_stack.clear()
            elif x == '*' and len(num) > 1:
                if len(num) < 2:
                    print('#{} {}'.format(t+1,'error'))
                    break
                cal_stack.append(num.pop())
                cal_stack.append(num.pop())
                num.append(cal_stack[-1]*cal_stack[0])
                cal_stack.clear()
            elif x =='/' and len(num) > 1:
                if len(num) < 2:
                    print('#{} {}'.format(t+1,'error'))
                    break
                cal_stack.append(num.pop())
                cal_stack.append(num.pop())
                if cal_stack[0] == 0:
                    print('#{} {}'.format(t+1,'error'))
                    break
                num.append(cal_stack[-1]//cal_stack[0])
                cal_stack.clear()
            elif x =='-' and len(num) > 1:
                if len(num) < 2:
                    print('#{} {}'.format(t+1,'error'))
                    break
                cal_stack.append(num.pop())
                cal_stack.append(num.pop())
                num.append(cal_stack[-1] - cal_stack[0])
                cal_stack.clear()
            elif x == '.':
                if len(num) == 1:
                    print('#{} {}'.format(t+1,num[0]))
                else:
                    print('#{} {}'.format(t+1,'error'))
    else:
        print('#{} {}'.format(t+1,'error'))

