a,b = map(int,input().split())
result = []
result.append(a+b)
result.append(a-b)
result.append(a*b)
result.append(a//b)
for x in result:
    print(x)