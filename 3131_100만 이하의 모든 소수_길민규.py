prime = [1] * 10000001
for i in range(2,1000001):
    if prime[i]:
        print(i, end=' ')
    j = 2
    while 1:
        if i * j > 1000000:
            break
        prime[j*i] = 0
        j += 1




