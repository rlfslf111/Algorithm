# import sys
# sys.stdin = open('mkpass.txt','r')

for t in range(10):
    tc = int(input())
    num_list = list(map(int,input().split()))

    while num_list[-1]!=0:
        i=1
        ap_list = []
        while i!=6:
            if num_list[-1] == 0:
                break
            move = num_list[0] - i
            if move <= 0:
                ap_list.append(0)
            else:
                ap_list.append(move)
            del num_list[0]
            num_list.append(ap_list[0])
            del ap_list[0]
            i+=1
    num_list = [str(_) for _ in num_list]
    print('#{} {}'.format(tc,' '.join(num_list)))