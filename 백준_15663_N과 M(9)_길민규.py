def perm(k):
    if k == M:
        print(*ans)
        return
    same = 0
    for i in range(N):
        if not check[i] and same != num_list[i]:
            check[i] = True
            ans.append(num_list[i])
            same = num_list[i]
            perm(k+1)
            ans.pop()
            check[i] = False

N, M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
check = [False] * N
ans = []
perm(0)






# def perm(k):
#     if k == M:
#         temp = [*ans]
#         if temp not in result:
#             result.append(temp)
#         return
#
#     for i in range(N):
#         if check[i]: continue
#         check[i] = True
#         ans.append(num_list[i])
#         perm(k+1)
#         ans.pop()
#         check[i] = False
#
# N, M = map(int,input().split())
# num_list = list(map(int,input().split()))
# num_list.sort()
# check = [False] * N
# ans = []
# result = []
# perm(0)
# for x in result:
#     print(*x)





