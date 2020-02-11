import sys
sys.stdin = open('palindrome1.txt','r')

for t in range(10):
    gesu = int(input())
    pal_list = [input() for _ in range(8)]

    count = 0
    # 가로 확인
    for y in range(8):
        for x in range(8-gesu+1):
            verify_list = []
            for k in range(x,x+gesu):
                verify_list.append(pal_list[y][k])

            flag = True
            for j in range(len(verify_list)//2):
                if verify_list[j] != verify_list[len(verify_list)-1-j]:
                    flag = False
            if flag:
                count+=1

    # 세로 확인
    for x in range(8):
        for y in range(8-gesu+1):
            verify_list2 = []
            for k in range(y,y+gesu):
                verify_list2.append(pal_list[k][x])
            flag = True
            for j in range(len(verify_list2)//2):
                if verify_list2[j] != verify_list2[len(verify_list2)-1-j]:
                    flag = False
            if flag:
                count+=1


    print('#{} {}'.format(t+1,count))
