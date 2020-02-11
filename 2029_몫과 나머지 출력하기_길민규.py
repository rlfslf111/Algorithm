def gar(a,b):
    result = a//b
    namugi = a%b
    list1 = [result,namugi]
    list1 = [str(_) for _ in list1]
    return ' '.join(list1)
test_case = int(input())
for x in range(test_case):
    a,b = map(int,input().split())
    print('#{} {}'.format(x+1,gar(a,b)))