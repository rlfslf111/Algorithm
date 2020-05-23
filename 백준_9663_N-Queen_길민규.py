def queen(k):
    if k == N:
        cnt[0] += 1
        return
    for i in range(N):
        if not check[i]:
            flag = False
            for j in range(k):
                if abs(k-j) == abs(i-ans[j]):
                    flag = True
                    break
            if flag:
                continue

            check[i] = True
            ans.append(i)
            queen(k+1)
            ans.pop()
            check[i] = False

N = int(input())

check = [False] * N
ans = []
cnt = [0]
queen(0)
print(cnt[0])



'''
N, ans = int(input()), [0]
# 놓여지는 위치를 기준으로
# 윗 직선, 오른쪽 대각위, 왼쪽 대각위
a, b, c = [False]*N, [False]*(2*N-1), [False]*(2*N-1)

def queen(k):
    if k == N:
        ans[0] += 1
        return
    for i in range(N):
        if (not a[i] and not b[k+i] and not c[k-i+N-1]):
            a[i] = b[k+i] = c[k-i+N-1] = True
            queen(k+1)
            a[i] = b[k+i] = c[k-i+N-1] = False
queen(0)
print(ans[0])
'''