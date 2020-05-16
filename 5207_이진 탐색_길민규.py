def find(goal, l, m, r, dir):
    if A[m] == goal:
        cnt[0] += 1
        return
    if l > r:
        return

    if goal > A[m]:
        if dir == 0:
            dir = 1
            find(goal, m+1, (m+1+r)//2, r, dir)
        else:
            return
    else:
        if dir == 1:
            dir = 0
            find(goal,l,(m-1+l)//2, m-1, dir)
        else:
            return

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort()

    l = 0
    r = len(A) - 1
    m = (l+r)//2

    # dir = 1 오른쪽, dir = 0 왼쪽
    cnt = [0]
    for b in range(len(B)):
        if B[b] < A[(len(B)-1)//2]:
            dir = 1
        else:
            dir = 0

        find(B[b], l, m, r, dir)


    print('#{} {}'.format(t,cnt[0]))
