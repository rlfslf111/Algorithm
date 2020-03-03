def solve(k,ans):
    ans = int(ans)
    if k == N:
        maxv[0] = max(maxv[0],ans)
        minv[0] = min(minv[0],ans)
    else:
        if oper[0] != 0:
            oper[0] -= 1
            solve(k+1,ans + num[k])
            oper[0] += 1
        if oper[1] != 0:
            oper[1] -= 1
            solve(k+1,ans - num[k])
            oper[1] += 1
        if oper[2] != 0:
            oper[2] -= 1
            solve(k+1,ans * num[k])
            oper[2] += 1
        if oper[3] != 0:
            oper[3] -= 1
            solve(k+1,ans / num[k])
            oper[3] += 1

N = int(input())
num = list(map(int,input().split()))
oper = list(map(int,input().split()))
maxv = [-1000000001]
minv = [1000000001]
solve(1,num[0])
print(maxv[0])
print(minv[0])