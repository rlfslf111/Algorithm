def combi(k):
    if k == 6:
        print(*ans)
    for i in range(N):
        if check[i]: continue
        check[i] = True
        ans.append(num_list[i])
        combi(k+1)
        ans.pop()
        for j in range(i+1,N):
            check[j] = False

while 1:
    input1 = list(map(int,input().split()))
    N = input1[0]
    if N == 0:
        break
    num_list = []
    for i in range(1,len(input1)):
        num_list.append(input1[i])
    check = [False] * N
    ans = []
    combi(0)
    print()
