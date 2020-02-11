su = int(input())
result = []
for x in range(1,su+1):
    if su%x == 0:
        result.append(x)
result = [str(_) for _ in result]
print(' '.join(result))