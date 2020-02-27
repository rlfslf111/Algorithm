def verify(ans):
    for x in range(ans[-1]+1):
        if x not in ans:
            return x

tc = int(input())
for t in range(tc):
    N = int(input())
    num_list = []
    while 1:
        num_list += list(input().split())
        if len(num_list) >= N:
            break

    ans = [int(num_list[-1])]
    for x in range(N-1):
        ans.append(int(num_list[x]))
        attach = ''
        for i in range(x,x+2):
            attach += num_list[i]
        ans.append(int(attach))

    for x in range(N-2):
        attach = ''
        for j in range(x,x+3):
            attach += num_list[j]
        ans.append(int(attach))
    ans.sort()

    print('#{} {}'.format(t+1,verify(ans)))
