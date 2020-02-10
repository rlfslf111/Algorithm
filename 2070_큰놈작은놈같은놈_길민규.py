def compare(a,b):
    if a>b:
        return '>'
    elif a<b:
        return '<'
    else:
        return '='
test_case=int(input())
for x in range(test_case):
    su1, su2 = map(int,input().split())
    print('#{} {}'.format(x+1,compare(su1,su2)))