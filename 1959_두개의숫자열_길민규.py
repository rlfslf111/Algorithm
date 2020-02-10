import sys
sys.stdin = open('two_string.txt','r')

tc = int(input())
for t in range(tc):
    A_length, B_length= map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    sum = 0
    multi_list = []
    i = 0
    if len(A) < len(B):
        while i < len(B)-len(A) +1:
            for a in range(len(A)):
                sum += A[a]*B[a+i]
            else:
                multi_list.append(sum)
                sum=0
            i+=1

    if len(B) < len(A):
        while i < len(A)-len(B)+1:
            for b in range(len(B)):
                sum += B[b]*A[b+i]
            else:
                multi_list.append(sum)
                sum = 0
            i+=1

    print('#{} {}'.format(t+1,max(multi_list)))