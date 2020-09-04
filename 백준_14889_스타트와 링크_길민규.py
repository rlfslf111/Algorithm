import sys
input = sys.stdin.readline

from itertools import combinations

def team2_member(tema1):
    team2 = [i for i in range(N)]
    for x in team1:
        if x in team2:
            team2.remove(x)
    return team2


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

minv = 1231231

member = [i for i in range(N)]
for i in combinations(member, N//2):
    # team1 과 team2를 구별한다.
    team1 = i
    team2 = team2_member(team1)


    # team1의 synerge를 계산한다.
    synerge1 = 0
    for s in combinations(team1,2):
        s1, s2 = s
        synerge1 += board[s1][s2] + board[s2][s1]

    # team2의 synerge를 계산한다.
    synerge2 = 0
    for s in combinations(team2,2):
        s1, s2 = s
        synerge2 += board[s1][s2] + board[s2][s1]

    minv = min(minv, abs(synerge1 - synerge2))


print(minv)



### 백트랙킹을 이용한 풀이
# def divide_team(depth):
#     if depth == N//2:
#         team2 = [k for k in range(N)]
#         for i in team1:
#             if i in team2:
#                 team2.remove(i)
#
#         synerge1 = 0
#         for i in range(len(team1) - 1):
#             for j in range(i + 1, len(team1)):
#                 synerge1 += board[team1[i]][team1[j]] + board[team1[j]][team1[i]]
#
#         synerge2 = 0
#         for i in range(len(team2) - 1):
#             for j in range(i + 1, len(team2)):
#                 synerge2 += board[team2[i]][team2[j]] + board[team2[j]][team2[i]]
#
#         minv[0] = min(minv[0], abs(synerge1 - synerge2))
#
#     else:
#         for i in range(N):
#             if not check[i]:
#                 check[i] = True
#                 team1.append(members[i])
#                 divide_team(depth + 1)
#                 team1.pop()
#                 for j in range(i + 1,N):
#                     check[j] = False
#
# N = int(input())
# board = [list(map(int,input().split())) for _ in range(N)]
#
# members = [i for i in range(N)]
# check = [False] * N
# team1 = []
# ans1 = []
# minv = [1231231]
# divide_team(0)
# print(minv[0])