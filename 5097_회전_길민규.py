from collections import deque

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    num = list(map(int,input().split()))
    q = deque()
    for i in range(len(num)):
        q.append(num[i])

    for k in range(M):
        stack = []
        stack.append(q.popleft())
        q.append(stack[0])
        del stack[0]

    print('#{} {}'.format(t,q.popleft()))