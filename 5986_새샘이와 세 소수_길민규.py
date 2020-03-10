# 3중 포문을 이용한 부분집합 구현 #
for t in range(1, int(input()) + 1):
    N = int(input())
    prime = [0, 0] + [1] * (N - 1)
    sieve = []
    for x in range(2, N + 1):
        if prime[x]:
            sieve += [x]
            att = ((N // x) - 1)
            prime[2 * x::x] = [0] * att
    cnt = 0
    for i in sieve:
        for j in sieve[sieve.index(i)::]:
            for k in sieve[sieve.index(j)::]:
                if N == i + j + k:
                    cnt += 1
    print('#{} {}'.format(t, cnt))
