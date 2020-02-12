# def verify(hay_list):
#     for x in range(len(hay_list)):
#         if hay_list[x] != hay_list[len(hay_list)-1-x]:
#             return False
#     return True
#
# tc = int(input())
# for t in range(tc):
#     hay_gesu = int(input())
#     hay_list = []
#     for h in range(hay_gesu):
#         hay_size = int(input())
#         hay_list.append(hay_size)
#
#     count = 0
#     while 1:
#         if verify(hay_list):
#             break
#         hay_list.sort()
#         hay_list[-1]-=1
#         hay_list[0]+=1
#         count+=1
#     print('#{} {}'.format(t+1,count))





#위의 코드는 정답은 맞는데 시간초과가 뜸
# 밑의 코드로 정답제출 완료

tc = int(input())
for t in range(tc):
    hay_gesu = int(input())
    hay_list = []
    for h in range(hay_gesu):
        hay_size = int(input())
        hay_list.append(hay_size)

    sum = 0
    for x in hay_list:
        sum += x
    avg = sum//hay_gesu

    ans = 0
    for x in range(hay_gesu):
        if hay_list[x] > avg:
            ans += hay_list[x] - avg
    print('#{} {}'.format(t+1,ans))