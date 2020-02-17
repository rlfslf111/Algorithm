import sys
sys.stdin = open('calculation.txt','r')

for t in range(10):
    length = int(input())
    math = input()
    stack = []
    num_list = []

    icp = {'*': 2, '+': 1, '(': 3}
    isp = {'*': 2, '+': 1, '(': 0}

    for i in range(length):
        if math[i].isdigit():
            num_list.append(math[i])
        else:
            # stack이 비어있으면 넣기
            if len(stack) == 0:
                stack.append(math[i])
                continue
            # stack이 비어있지 않을 때
            elif len(stack) > 0:
                if math[i] == ')':
                    while stack[-1] != '(':
                        num_list.append(stack.pop())
                    stack.pop()

                elif icp[math[i]] > isp[stack[-1]]:
                    stack.append(math[i])
                else:
                    while icp[math[i]] <= isp[stack[-1]]:
                        num_list.append(stack.pop())
                    stack.append(math[i])

    #계산 시작
    for i in range(len(num_list)):
        if num_list[i].isdigit():
            stack.append(num_list[i])
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            result = 0
            if num_list[i] == '+':
                result = num1 + num2
            elif num_list[i] == '*':
                result = num1 * num2
            stack.append(result)
    print('#{} {}'.format(t+1,stack[0]))



