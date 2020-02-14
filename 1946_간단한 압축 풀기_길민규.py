test_case = int(input())
for x in range(test_case):
    empty = ''
    howmany_alphabet = int(input())
    for i in range(howmany_alphabet):
        a,b = list(map(str,input().split()))
        empty += a*int(b)
    print('#{}'.format(x+1))
    good = ''
    for x in empty:
        good+=x
        if len(good)%10==0:
            print(good)
            good=''
    print(good)