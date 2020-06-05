import sys
sys.stdin = open('input.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    D = [0 for _ in range(N)]
    root = 0
    for i in range(1,N):
        D[i] = ((X[root] - X[i])**2 + (Y[root]-Y[i])**2) * E

    ans = 0
    visit = [0 for _ in range(N)]
    visit[root] = 1
    standard = 0

    for y in range(N - 1):
        minv = 12345678987654321
        for x in range(N):
            if not visit[x] and D[x] < minv:
                minv = D[x]
                standard = x

        ans += minv
        visit[standard] = 1
        root = standard

        for i in range(N):
            if not visit[i]:
                cost = ((X[root] - X[i])**2 + (Y[root]-Y[i])**2) * E
                if cost < D[i]:
                    D[i] = cost

    print('#{} {}'.format(t,round(ans)))



# 크루스칼을 사용한 방법

# from queue import  PriorityQueue
#
# # 크루스칼 단거리 찾기
# def find(x):
#     if root[x] != x:
#         root[x] = find(root[x])
#     return root[x]
#
# # 싸이클을 찾기위한 병합
# def combine(x,y):
#     a = find(x)
#     b = find(y)
#     if a > b:
#         root[a] = b
#     else:
#         root[b] = a
#
# for t in range(1,int(input())+1):
#     N = int(input())
#     X = list(map(int,input().split()))
#     Y = list(map(int,input().split()))
#     E = float(input())
#
#     distance = PriorityQueue()
#
#     for i in range(N):
#         for j in range(i+1,N):
#             d =((X[i]-X[j])**2 + (Y[i]-Y[j])**2) ** 0.5
#             distance.put((d,i,j))
#
#     cnt = 0
#     ans = 0
#     root = [i for i in range(N)]
#
#     while distance and cnt != N - 1:
#         dis, x, y = distance.get()
#         if find(x) != find(y):
#             ans += (dis**2) * E
#             cnt += 1
#             combine(x,y)
#     ans = int(ans + 0.5)
#     print('#{} {}'.format(t,ans))





