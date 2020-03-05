import sys
sys.stdin = open('input.txt','r')

tc = int(input())
for t in range(1,tc+1):
    N = int(input())
    num = list(map(int,input().split()))

    ans = [1] + [0] * 10000
    maxv = 0
    for i in range(len(num)):
        maxv += num[i]
        ans[maxv] = -1
        for j in range(maxv):
            if ans[j] == 1 and ans[j+num[i]] == 0:
                ans[j+num[i]] = -1
        for j in range(maxv+1):
            if ans[j] == -1:
                ans[j] = 1
    print('#{} {}'.format(t,ans.count(1)))


# 부분집합 비트연산을 이용한 풀이
# tc = int(input())
# for t in range(1,tc+1):
#     N = int(input())
#     num_list = list(map(int,input().split()))
#
#     ans = set()
#     for i in range(1<<N):
#         sum = 0
#         for j in range(N):
#             if i & (1<<j):
#                 sum += num_list[j]
#         if sum in ans:
#             continue
#         ans.add(sum)
#     print('#{} {}'.format(t,len(ans)))


# 부분집합 제귀호출을 이용한 풀이
# def sub(k,sum):
#     if k == N:
#         ans.add(sum)
#         return
#     if sum in ans:
#         return
#     else:
#         sub(k+1,sum+num_list[k])
#         sub(k+1,sum)
#
# tc = int(input())
# for t in range(1,tc+1):
#     N = int(input())
#     num_list = list(map(int,input().split()))
#     check = [0] * N
#     ans = set()
#     sub(0,0)
#     print('#{} {}'.format(t,len(ans)))





