import sys
sys.stdin = open('aaa.txt','r')

# tc = int(input())
# for t in range(1,tc+1):
#     word = input()
#     stack = []
#     flag = True
#
#     for i in range(len(word)):
#         if word[i] == '(' or word[i] == '{':
#             stack.append(word[i])
#         elif word[i] == ')':
#             if len(stack) > 0 and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 flag =False
#                 break
#         elif word[i] == '}':
#             if len(stack) > 0 and stack[-1] =='{':
#                 stack.pop()
#             else:
#                 flag =False
#                 break
#
#     if flag and len(stack) == 0:
#         print('#{} {}'.format(t,1))
#
#     else:
#         print('#{} {}'.format(t,0))






tc = int(input())
for t in range(tc):
    word = input()

    stack_list = []
    flag = True
    for x in range(len(word)):
        if word[x] =='(' or word[x] =='{':
            stack_list.append(word[x])
        elif word[x] == ')':
            if len(stack_list) > 0 and stack_list[-1] == '(':
                stack_list.pop()
            else:
                flag = False
                break
        elif word[x] == '}':
            if len(stack_list) > 0 and stack_list[-1] == '{':
                stack_list.pop()
            else:
                flag = False
                break
    if flag and len(stack_list) == 0:
        print('#{} {}'.format(t+1,1))
    else:
        print('#{} {}'.format(t + 1, 0))