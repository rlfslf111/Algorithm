from collections import deque

def find_parent():
    q1 = deque()
    q2 = deque()
    q1.append(x1)
    q2.append(x2)
    visit1[x1] = 1
    visit2[x2] = 1
    while q1:
        v1 = q1.popleft()
        for e in check_p[v1]:
            if not visit1[e]:
                visit1[e] = 1
                q1.append(e)

    while q2:
        v2 = q2.popleft()
        if visit1[v2]:
            return v2
        for e in check_p[v2]:
            if not visit2[e]:
                visit2[e] = 1
                q2.append(e)

def find_child(mother):
    q = deque()
    q.append(mother)
    visit = [0 for _ in range(V+1)]
    visit[mother] = 1
    cnt = 1
    while q:
        v = q.popleft()
        for e in check_c[v]:
            if not visit[e]:
                visit[e] = 1
                cnt += 1
                q.append(e)
    return cnt


for t in range(1,int(input())+1):
    V, E, x1, x2 = map(int,input().split())
    check_p = [[] for _ in range(V+1)]
    check_c = [[] for _ in range(V+1)]
    line = list(map(int,input().split()))
    for i in range(0,2*E,2):
        check_p[line[i+1]].append(line[i])
        check_c[line[i]].append(line[i+1])
    visit1 = [0 for _ in range(V+1)]
    visit2 = [0 for _ in range(V+1)]

    mother = find_parent()
    print('#{} {} {}'.format(t,mother,find_child(mother)))