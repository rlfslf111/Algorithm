def solve():
    for i in range(10):
        num[1][i] = 1
    for y in range(2,N+1):
        for x in range(10):
            for k in range(x+1):
                num[y][x] += num[y-1][k]

N = int(input())
num = [[0]*10 for _ in range(N+1)]
tr = 10007
solve()
print(sum(num[N])%tr)

