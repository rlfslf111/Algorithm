N = int(input())
time = []
pay = []
benefit = [0] * (N+1)
for n in range(N):
    T, P = map(int,input().split())
    time.append(T)
    pay.append(P)

for i in range(N-1,-1,-1):
    if time[i] + i > N:
        benefit[i] = benefit[i+1]
    else:
        benefit[i] = max(benefit[i+1], pay[i]+benefit[i+time[i]])
print(benefit[0])




# N = int(input())
# T, P = [], []
# for n in range(N):
#     t, p = map(int, input().split())
#     T.append(t)
#     P.append(p)
# mymax = [0]
# order = []
#
# def DFS(k, money):
#     if k == N:
#         if money > mymax[0]:
#             mymax[0] = money
#     for i in range(k, N):
#         if i + T[i] > N:
#             continue
#         else:
#             DFS(i+T[i], money+P[i])
#     else:
#         if money > mymax[0]:
#             mymax[0] = money
#
# DFS(0, 0)
# print(mymax[0])