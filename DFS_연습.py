def dfs(visited,V):
    print(V, end=' ')
    for i in range(1,N+1):
        if arr[V][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited,i)


N, M = map(int,input().split())

arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    st, ed = map(int,input().split())
    arr[st][ed] = arr[ed][st] = 1

for i in range(N+1):
    print(arr[i])

dfs([1],1)


# 입력 값
# 정점의 갯수 N 과 간선의 갯수 M이 주어지고
# M개의줄에 걸쳐 간선의 정보가 주어진다.
# 인접행렬을 구현하고 DFS 탐색한 결과를 출력하여라
# 시작정점은 1브타
# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7


