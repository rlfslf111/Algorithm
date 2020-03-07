tc = int(input())
for t in range(1,tc+1):
    A, B = map(int,input().split())

    print('#{} {}'.format(t,(A//B)**2))