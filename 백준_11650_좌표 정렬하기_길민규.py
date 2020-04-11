N = int(input())
ans = []
for n in range(N):
    ans.append(list(map(int,input().split())))

result = sorted(ans, key=lambda x : (x[0],x[1]))
for i in range(len(result)):
    print(*result[i])
