from collections import deque
def bfs(v):
    q = deque()
    visit = [0] * (N+1)
    q.append(v)
    visit[v] = 1
    cnt = 1
    while q:
        v = q.popleft()
        # v index에 들어있는 check[v]의 숫자들을 모두 센다.
        for k in check[v]:
            if not visit[k]:
                q.append(k)
                visit[k] = 1
                cnt += 1
    return cnt

N, M  = map(int,input().split())
check = [[] for _ in range(N+1)]
for m in range(M):
    A, B = map(int,input().split())
    check[B].append(A)

maxl = 0
ans = []
for i in range(1,N+1):
    c = bfs(i)
    # max 값과 같으면 추가
    if c == maxl:
        ans.append(i)
    # max 값을 갱신할 때 배열도 초기화
    elif c > maxl:
        ans = [i]
        maxl = c
ans.sort()
print(*ans)
