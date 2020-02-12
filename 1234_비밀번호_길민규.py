import sys
sys.stdin = open('password.txt','r')

for t in range(10):
    length, num = input().split()
    num = [str(_) for _ in num]

    ans = []
    ans.append(num[0])
    for x in range(1,len(num)):
        if len(ans) > 0:
            if ans[-1] == num[x]:
                ans.pop()
                continue
        if len(ans) == 0:
            ans.append(num[x])
        elif ans[-1] != num[x]:
            ans.append(num[x])

    print('#{} {}'.format(t+1,''.join(ans)))





