# DP (Dynamic Programming)을 이용한 풀이
for t in range(1,int(input())+1):
    N = int(input())
    num = list(map(int,input().split()))
    dp = [0] * N

    maxv = 0
    for i in range(N):
        dp[i] = 1
        for j in range(0,i):
            if num[j] < num[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
        maxv = max(maxv,dp[i])
    print(dp)
    print('#{} {}'.format(t,maxv))
