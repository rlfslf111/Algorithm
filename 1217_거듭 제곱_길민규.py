def square(su,sueng):
    if seung == 0:
        return 1
    if sueng == 1:
        return su
    return square(su,sueng-1)*su

for t in range(10):
    tc = int(input())
    su, seung = map(int,input().split())
    print('#{} {}'.format(t+1,square(su,seung)))