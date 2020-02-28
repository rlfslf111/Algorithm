# import sys
# sys.stdin = open('input.txt','r')

def cal(k,num):
    num = int(num)
    if k == N:
        max_num[0] = max(max_num[0],num)
        min_num[0] = min(min_num[0],num)
    else:
        if operator[0] != 0:
            operator[0] -= 1
            cal(k+1, num + number[k])
            operator[0] += 1

        if operator[1] != 0:
            operator[1] -= 1
            cal(k+1, num - number[k])
            operator[1] += 1

        if operator[2] != 0:
            operator[2] -= 1
            cal(k+1, num * number[k])
            operator[2] += 1

        if operator[3] != 0:
            operator[3] -= 1
            cal(k+1, num / number[k])
            operator[3] += 1

tc = int(input())
for t in range(1,tc+1):
    N = int(input())
    operator = list(map(int,input().split()))
    number = list(map(int,input().split()))
    max_num = [-123123123]
    min_num = [123123123]
    # 첫 번째 자리의 숫자는 고정으로 가지고 함수에 들어간다.
    cal(1,number[0])
    print('#{}'.format(t),max_num[0]-min_num[0])

