from collections import deque
def tree(v):
    q = deque()
    q.append(v)
    visit = [0] * (E*2)
    visit[v] = 1
    cnt = 1
    while q:
        v = q.popleft()
        for e in check[v]:
            if not visit[e]:
                visit[e] = 1
                cnt += 1
                q.append(e)
    return cnt

for t in range(1,int(input())+1):
    E, N = map(int,input().split())
    num_list = list(map(int,input().split()))
    check = [[] for _ in range(E+2)]
    for i in range(0,len(num_list),2):
        check[num_list[i]].append(num_list[i+1])

    print('#{} {}'.format(t,tree(N)))