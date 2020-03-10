for t in range(1,int(input())+1):
    D, A, B = map(int,input().split())
    prime = [0, 0] + [1] * (B - 1)
    sieve = []
    for x in range(2, B + 1):
        if prime[x]:
            att = ((B // x) - 1)
            prime[2 * x::x] = [0] * att
        if prime[x] and x >= A:
            sieve += [str(x)]
    cnt = 0
    for i in range(len(sieve)):
        if str(D) in sieve[i]:
            cnt += 1
    print('#{} {}'.format(t,cnt))