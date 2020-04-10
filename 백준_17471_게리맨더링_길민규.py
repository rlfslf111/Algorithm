from itertools import combinations
from collections import deque

# sec1과 sec2를 2개의 구역으로 분할한다.
def divide(sec):
    temp = list(range(1,N+1))
    for i in sec:
        temp.remove(i)
    return tuple(temp)

# 나뉘어진 구역이 타당하게 나뉘었는지를 검사한다.
def verify(section,gaesu):
    q = deque()
    visit[section[0]] = 1
    q.append(section[0])
    count = 1

    while q:
        v = q.popleft()
        for k in region[v]:
            if k in section and not visit[k]:
                visit[k] = 1
                count += 1
                q.append(k)

    if count == gaesu:
        return True
    else:
        return False

# 타당하게 나뉘어진 구역이라면 인구를 센다.
def population(section):
    person = 0
    for i in section:
        person += people[i]
    return person


N = int(input())
people = [0] + list(map(int,input().split()))
region = [[] for _ in range(N+1)]
for n in range(1,N+1):
    component = list(map(int,input().split()))
    for s in range(1,len(component)):
        region[n].append(component[s])

minv = 1231231

# 1개부터 N//2개 까지 구역을 2개로 나누어준다.
for i in range(1,(N//2)+1):
    for sec1 in combinations(range(1,N+1),i):
        sec2 = divide(sec1)
        visit = [0] * (N+1)
        # 나뉜 구역이 타당하게 나뉜것이라면,
        if verify(sec1,i) and verify(sec2,N-i):
            minv = min(minv,abs(population(sec1) - population(sec2)))

if minv != 1231231:
    print(minv)
else:
    print(-1)