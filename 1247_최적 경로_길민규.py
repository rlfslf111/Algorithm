from itertools import permutations

def go(k):
    x, y = company
    distance = 0
    for i in range(len(k)):
        if distance >= minv[0]:
            return
        distance += abs(x - k[i][0]) + abs(y - k[i][1])
        x, y = k[i][0], k[i][1]
    hx, hy = home
    distance += abs(x - hx) + abs(y - hy)
    minv[0] = min(distance,minv[0])

for t in range(1,int(input())+1):
    N = int(input())
    location = list(map(int,input().split()))

    company = [location[0],location[1]]
    home = [location[2],location[3]]

    customer = []
    for i in range(4,len(location),2):
        customer.append([location[i],location[i+1]])

    minv = [1231231]
    for k in permutations(customer,N):
        go(k)
    print('#{} {}'.format(t,minv[0]))