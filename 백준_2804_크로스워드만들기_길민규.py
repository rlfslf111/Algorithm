A,B = input().split()
board = [['.']*len(A) for _ in range(len(B))]

idx_A = 0
idx_B = 0
for i in range(len(A)):
    flag = False
    for j in range(len(B)):
        if A[i] == B[j]:
            idx_A = j
            idx_B = i
            flag = True
            break
    if flag:
        break

for y in range(len(B)):
    for x in range(len(A)):
        board[idx_A][x] = A[x]
for x in range(len(A)):
    for y in range(len(B)):
        board[y][idx_B] = B[y]

for i in range(len(B)):
    print(''.join(map(str,board[i])))