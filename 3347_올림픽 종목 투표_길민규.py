for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    vote = [0] * len(A)

    i = 0
    while i != len(B):
        for x in range(len(A)):
            if B[i] >= A[x]:
                vote[x] += 1
                break
        i += 1

    ans = vote.index(max(vote))
    print('#{} {}'.format(t,ans+1))