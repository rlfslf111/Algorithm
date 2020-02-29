import sys
sys.stdin = open('input.txt','r')

from itertools import combinations

def com(k):
    if k == N//2:
        ans = combi[:]
        result.append(ans)
    for i in range(N):
        if not check[i]:
            check[i] = True
            combi.append(index[i])
            com(k+1)
            combi.pop()
            for j in range(i+1,N):
                check[j] = False

tc = int(input())
for t in range(1,tc+1):
    N = int(input())
    synerge = [list(map(int,input().split())) for _ in range(N)]

    index = list(range(N))
    check = [False] * N
    combi = []
    result = []
    com(0)
    result2 = result[:]
    result2.reverse()

    ans = []
    for i in range(len(result)//2):
        A_taste, B_taste = 0, 0
        for j in combinations(result[i],2):
            cook1, cook2 = j[0], j[1]
            A_taste += (synerge[cook1][cook2] + synerge[cook2][cook1])
        for k in combinations(result2[i],2):
            cook1, cook2 = k[0], k[1]
            B_taste += (synerge[cook1][cook2] + synerge[cook2][cook1])
        ans.append(abs(A_taste-B_taste))
    print('#{} {}'.format(t,min(ans)))





#set의 difference를 이용한 풀이

# tc = int(input())
# for t in range(1, tc + 1):
#     N = int(input())
#     r = N // 2
#     synerge = [list(map(int, input().split())) for _ in range(N)]
#
#     s = set(range(N))
#     s1 = list(combinations(s,r))
#     s2 = [tuple(s.difference(s1[i])) for i in range(len(s1))]
#
#     ans = []
#     for i in range(len(s1)//2):
#         so1, so2 = 0, 0
#         for j in combinations(s1[i],2):
#             cook1, cook2 = j[0], j[1]
#             so1 += (synerge[cook1][cook2] + synerge[cook2][cook1])
#         for k in combinations(s2[i],2):
#             cook1, cook2 = k[0], k[1]
#             so2 += (synerge[cook1][cook2] + synerge[cook2][cook1])
#         ans.append(abs(so1-so2))
#     print('#{} {}'.format(t,min(ans)))
