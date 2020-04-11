N = int(input())
ans = []
for n in range(N):
    ans.append(list(map(int,input().split())))

result = sorted(ans, key=lambda x : (x[1],x[0]))
for i in range(len(result)):
    print(*result[i])