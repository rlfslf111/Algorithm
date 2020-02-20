# 순열을 사용해서 해결한 결과
def find(k):
    global flag
    if sum(ans) > 100:
        return
    if k == 7 and sum(ans) == 100:
        flag = True
        ans.sort()
        for j in range(len(ans)):
            print(ans[j])
    for i in range(N):
        if check[i]: continue
        check[i] = True
        ans.append(hobit_list[i])
        find(k+1)
        if flag:
            return
        check[i] = False
        ans.pop()

hobit_list = []
for h in range(9):
    tall = int(input())
    hobit_list.append(tall)
N = len(hobit_list)
check = [False] * N
flag = False
ans = []
find(0)



# 부분집합을 사용해서 해결한 결과
# def find(N):
#     for i in range(1<<N):
#         ans = []
#         for j in range(N):
#             if i & (1<<j):
#                 ans.append(hobit_list[j])
#             if sum(ans) == 100 and len(ans) == 7:
#                 return ans
#
# hobit_list = []
# for h in range(9):
#     hobit_list.append(int(input()))
# N = len(hobit_list)
# result = find(N)
# result.sort()
# for i in range(len(result)):
#     print(result[i])






