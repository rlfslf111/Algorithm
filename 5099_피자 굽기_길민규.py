from collections import deque

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    pizza_list = list(map(int,input().split()))

    pizza = deque()
    for p in range(M):
        pizza.append((pizza_list[p],p+1))

    q = deque()

    for n in range(N):
        q.append(pizza.popleft())

    while 1:
        cheeze, idx = q.popleft()
        cheeze//=2
        if cheeze == 0 and len(pizza) > 0:
            q.append(pizza.popleft())
        elif cheeze != 0:
            q.append((cheeze,idx))
        if len(q) == 1 and len(pizza) == 0:
            print('#{} {}'.format(t,q[0][1]))
            break
