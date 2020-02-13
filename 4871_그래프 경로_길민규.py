import sys
sys.stdin = open('graph.txt','r')

def dfs(visited,T):
    for i in range(1,V+1):
        if arr[T][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited,i)
    return visited

tc = int(input())
for t in range(tc):
    V, E = map(int,input().split())   # V = Node, E = line
    arr = [[0]*(V+1) for _ in range(V+1)]
    for e in range(E):
        st, ed = map(int,input().split())
        arr[st][ed] = 1

    S, G = map(int,input().split())

    for i in range(V+1):
        print(arr[i])
    print(dfs([S],S))

    if G in dfs([S],S):
        print('#{} {}'.format(t+1,1))
    else:
        print('#{} {}'.format(t + 1, 0))
