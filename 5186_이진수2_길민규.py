def binary(num):
    global result
    while 1:
        next = num * 2
        result += str(int(next))
        num = next - int(next)
        cnt[0] += 1
        if num == 0.0:
            return
        if cnt[0] > 13:
            return

for t in range(1,int(input())+1):
    N = float(input())
    result = ''
    cnt = [0]
    binary(N)

    if cnt[0] > 13:
        print('#{} overflow'.format(t))
    else:
        print('#{} {}'.format(t,result))