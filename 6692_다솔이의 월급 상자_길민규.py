tc = int(input())
for t in range(tc):
    N = int(input())

    avg = 0
    for s in range(N):
        p1, x1 = map(float,input().split())
        avg += p1*x1
    print('#%d %0.6f' %(t+1, avg))
