initial = [0,1,1,1] + list(0 for _ in range(100))

for i in range(4,101):
    initial[i] = initial[i-2] + initial[i-3]

tc = int(input())
for t in range(1,tc+1):
    print('#{} {}'.format(t,initial[int(input())]))

