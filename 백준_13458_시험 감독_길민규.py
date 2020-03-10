N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())

master = len(A)
for i in range(len(A)):
    A[i] -= B
    if A[i] <= 0:
        continue
    master += (A[i]-1)//C + 1
print(master)
