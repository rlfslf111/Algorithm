tc = int(input())
for t in range(tc):
    P,Q,R,S,W = map(int,input().split())
    A_fee = P*W
    if W < R:
        B_fee = Q
    if W > R:
        B_fee = Q + (W - R)*S
    if A_fee > B_fee:
        print('#{} {}'.format(t+1,B_fee))
    if B_fee > A_fee:
        print('#{} {}'.format(t+1,A_fee))