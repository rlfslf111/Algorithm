road = int(input())
road_list = list(map(int,input().split()))

pre = road_list[0]
max = 0
temp = [road_list[0]]
for x in road_list[1:]:
    if x > pre:
        temp.append(x)
        pre = x
    elif x <= pre:
        x_d = temp[-1] - temp[0]
        if x_d > max:
            max = x_d
        temp = [x]
    pre = x
if len(temp) >= 2:
    x_d = temp[-1] - temp[0]
    if x_d > max:
        max = x_d
print(max)


