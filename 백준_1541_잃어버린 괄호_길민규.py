problem = input().split('-')
ans = 0
for i in problem[0].split('+'):
    ans += int(i)

for i in problem[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)