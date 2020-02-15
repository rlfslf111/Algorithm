import sys
sys.stdin = open('work.txt','r')

def dfs(arr,reverse,s):
    result = []
    stack = [s]
    visited = [0]*(len(arr)+1)
    while stack:
        order = stack[-1]
        if not visited[order]:
            result.append(order)
        visited[order] = 1
        flag = False
        for i in arr[order]:
            if order in reverse[i]:
                reverse[i].remove(order)
            if not visited[i] and not reverse[i]:
                stack.append(i)
                flag = True
                break
        if not flag:
            stack.pop()
    return result

def solution(arr,reverse,start_point):
    n = len(arr)-1
    result = []
    for i in start_point:
        result += dfs(arr,reverse,i)
        if len(result) == n:
            return result
    return result

for t in range(1):
    V, E = map(int,input().split())
    work = list(map(int,input().split()))

    arr = [[] for _ in range(V+1)]
    reverse = [[] for _ in range(V+1)]

    for x in range(0,len(work),2):
        arr[work[x]].append(work[x+1])
        reverse[work[x+1]].append(work[x])
    start_point = []
    for i in range(1,V+1):
        if not reverse[i]:
            start_point.append(i)

    ans = solution(arr,reverse,start_point)
    ans = [str(_) for _ in ans]
    print('#{} {}'.format(t+1,' '.join(ans)))





#강사님 풀이

# def DFS(v):
#     visit[v] = True  # 노드 방문했으니 visit 추가
#     for w in G[v]:  # 해당 작업의 후행 작업 순회
#         if not visit[w]:  # 만약 해당 작업이 끝나지 않았으면, 작업 수행
#             DFS(w)
#     stack.append(v)  # 반복문이 끝이나면, V 작업의 후행 작업을 모두
#
#
# for test_case in range(1, 11):
#     V, E = map(int, input().split())
#
#     G = [[] for i in range(V + 1)]  # 그래프 생성, 각 작업을 선행으로 필요로 하는 작업 리스트
#     visit = [False] * (V + 1)  # 방문 배열
#     in_degree = [0] * (V + 1)  # 특정 작업의 선행작업 개수를 세기 위한 배열
#     stack = []  # 스택
#
#     arr = list(map(int, input().split()))
#     for i in range(0, E):
#         u, v = arr[i * 2], arr[i * 2 + 1]  # 간선 입력
#         G[u].append(v)  # 유향 그래프    # 그래프에 추가
#         in_degree[v] += 1  # 선행작업 개수 증가
#
#     for i in range(1, V + 1):
#         if in_degree[i] == 0:  # 선행작업이 없는 노드는, 작업 시작
#             DFS(i)  # dfs
#
#     print("#%d " % test_case, end='')
#     print(*stack[::-1])







# 강사님 풀이 2

# for tc in range(1, 11):
#     V, E = map(int, input().split())
#     arr = [[0] * (V + 1) for _ in range(V + 1)]
#     edges = list(map(int, input().split()))
#     prev_arr = [[0] * (V + 1) for _ in range(V + 1)]
#     order = list()
#     used = [0] * (V + 1)
#
#     for i in range(0, len(edges), 2):
#         st, ed = edges[i], edges[i + 1]
#         arr[st][ed] = 1
#         prev_arr[ed][st] = 1
#
#     for i in range(1, len(prev_arr)):
#         if prev_arr[i].count(1) == 0:
#             order.append(i)
#             used[i] = 1
#
#     while len(order) != V:
#         for i in range(1, V + 1):
#             if used[i] == 0:
#                 for j in range(1, V + 1):
#                     if prev_arr[i][j] == 1:
#                         if used[j] == 0:
#                             break
#                 else:
#                     order.append(i)
#                     used[i] = 1
#
#     print("#{}".format(tc), end=" ")
#     for i in order:
#         print(i, end=" ")
#     print()










