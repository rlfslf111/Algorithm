import sys
input = sys.stdin.readline

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visit = [1] + [0 for _ in range(N+2)]
    visit[start] = 1

    while q:
        go = q.popleft()
        if go == N + 2:
            return 'happy'
        for e in line[go]:
            if not visit[e]:
                visit[e] = 1
                q.append(e)

    return 'sad'

for t in range(int(input())):
    N = int(input())

    line = [[] for _ in range(N+3)]

    mapping = []
    for i in range(N+2):
        x, y = map(float,input().split())
        mapping.append((x,y))

    for i in range(len(mapping) - 1):
        for j in range(i+1,len(mapping)):
            if (abs(mapping[i][0] - mapping[j][0]) + abs(mapping[i][1] - mapping[j][1])) <= 1000:
                line[i+1].append(j+1)
                line[j+1].append(i+1)

    ans = []
    print(bfs(1))
