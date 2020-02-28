import sys
sys.stdin = open('input.txt','r')

def top(k, sum):
    if sum >= B:
        if sum < min[0]:
            min[0] = sum
    for i in range(N):
        if not check[i]:
            check[i] = True
            top(k+1, sum+clerk_H[i])
            for j in range(i+1, N):
                check[j] = False

tc = int(input())
for t in range(1,tc+1):
    N, B = map(int,input().split())
    clerk_H = list(map(int,input().split()))
    min = [1231231]
    check = [False] * N
    top(0, 0)
    print('#{} {}'.format(t,min[0]-B))


# 부분집합을 활용한 문제 해결 (but, 시간 초과)
    # min = 1231231
    # for i in range(1<<len(clerk_H)):
    #     sum = 0
    #     for j in range(len(clerk_H)):
    #         if i & (1<<j):
    #             sum += clerk_H[j]
    #         if sum >= B:
    #             if sum < min:
    #                 min = sum
    #                 break
    # print('#{} {}'.format(t,min-B))




