for t in range(1,int(input())+1):
    a, b = input().split()

    A = list(a)
    B = list(b)

    cnt = 0
    skip = 0
    for i in range(len(A)):
        if skip:
            skip -= 1
            continue
        if i <= len(A) - len(B) + 1 and A[i:i+len(B)] == B[:]:
            skip = len(B) - 1
        cnt += 1

    print('#{} {}'.format(t,cnt))


