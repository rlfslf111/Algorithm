def con(cnt):
    if cnt == M:
        print(*ans)
        return
    for i in range(N):
        if check[i]: continue
        ans.append(num_list[i])
        con(cnt+1)
        check[i] = True # True check를 재귀 호출 후 실행하여 중복 허용
        ans.pop()
        for j in range(i+1,N): # 오름차순을 위해 큰 트리의 위의 것을 False로 변환
            check[j] = False

N, M = map(int,input().split())
num_list = list(range(1,N+1))
check = [False] * N
ans = []
con(0)