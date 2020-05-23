import sys
sys.setrecursionlimit(10**8)

def dfs(k):
    if visit[k]:
        if k in ans:
            num = ans.index(k)
            result[0] += num
        else:
            result[0] += len(ans)
        return
    visit[k] = True
    ans.append(k)
    dfs(students[k])

for t in range(1,int(input())+1):
    N = int(input())
    students = [0] + list(map(int,input().split()))
    visit = [0 for _ in range(N+1)]

    result = [0]

    for i in range(1,N+1):
        if not visit[i]:
            ans = []
            dfs(i)
    print(result[0])