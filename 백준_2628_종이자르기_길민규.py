R,C = map(int,input().split())
cut_try = int(input())

R_list = [0]
C_list = [0]
for c in range(cut_try):
    direction, boundary = map(int,input().split())
    if direction == 0:
        C_list.append(boundary)
    if direction == 1:
        R_list.append(boundary)
R_list.append(R); R_list.sort()
C_list.append(C); C_list.sort()

area = []
for i in range(len(R_list)-1):
    for j in range(len(C_list)-1):
        area.append((R_list[i+1]-R_list[i])*(C_list[j+1]-C_list[j]))
print(max(area))