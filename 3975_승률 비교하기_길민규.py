ans = []
for t in range(1,int(input())+1):
    ratio = input().split()
    a = int(ratio[0])/int(ratio[1])
    b = int(ratio[2])/int(ratio[3])
    if a > b:
        result = "ALICE"
    else:
        if a < b:
            result = "BOB"
        else:
            result = "DRAW"
    ans.append(result)

j = 1
for i in ans:
    print('#{} {}'.format(j,i))
    j += 1
