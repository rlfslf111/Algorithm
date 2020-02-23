tc = int(input())
for t in range(tc):
    A, B, C = map(int,input().split())
    if A < B:
        print('#{} {}'.format(t+1,C//A))
    if B < A:
        print('#{} {}'.format(t+1,C//B))