def combination(count):
    if count == M:
        print(*ans)
        return
    for i in range(N):

        ans.append(num_list[i])
        combination(count+1)
        ans.pop()

N, M = map(int,input().split())
num_list = list(range(1,N+1))
# check = [False] * N  중복검사 부분만 제거하면 된다.
ans = []
combination(0)


