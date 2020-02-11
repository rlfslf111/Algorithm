import sys
sys.stdin = open('palindrome2.txt','r')

for t in range(10):
    order = int(input())
    pal_list = [input() for _ in range(100)]

    # 가로 확인
    count_list = []
    for y in range(100):
        for x in range(100):

            ans = []
            for k in range(x,100):
                ans.append(pal_list[y][k])

                count = 0
                for i in range(len(ans)):
                    if ans[i] == ans[len(ans)-1-i]:
                        count+=1
                    if ans[i] != ans[len(ans)-1-i]:
                        break
                count_list.append(count)

    # 세로 확인
    for x in range(100):
        for y in range(100):

            ans2 = []
            for k in range(y,100):
                ans2.append(pal_list[k][x])

                count = 0
                for i in range(len(ans2)):
                    if ans2[i] == ans2[len(ans2)-1-i]:
                        count+=1
                    if ans2[i] != ans2[len(ans2)-1-i]:
                        break
                count_list.append(count)

    print('#{} {}'.format(t+1,max(count_list)))