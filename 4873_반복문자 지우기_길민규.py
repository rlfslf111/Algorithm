tc = int(input())
for t in range(tc):
    word = list(input())
    ans = []
    ans.append(word[0])
    for x in range(1,len(word)):
        if len(ans) > 0:
            if ans[-1] == word[x]:
                ans.pop()
                continue
        if len(ans) == 0:
            ans.append(word[x])
        elif ans[-1] != word[x]:
            ans.append(word[x])

    print('#{} {}'.format(t+1,len(ans)))