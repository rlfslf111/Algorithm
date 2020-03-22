def hanoi(n,a,b,c):
    if n==1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)
N=int(input())
cur=0
i=0
while i<N:
    cur=(2*cur)+1
    i+=1

print(cur)
hanoi(N,1,2,3)

