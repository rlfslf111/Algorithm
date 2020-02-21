def password(k):
    result = ''
    vowel = 'aeiou'
    consonant = 'bcdfghjklmnopqrstvwxyz'
    cnt_v = 0
    cnt_c = 0
    if k == L:
        for x in range(len(ans)):
            result+=ans[x]
        for v in result:
            if v in vowel:
                cnt_v += 1
        for c in result:
            if c in consonant:
                cnt_c += 1
        if cnt_v > 0 and cnt_c > 1:
            print(result)
    for i in range(C):
        if check[i]: continue
        check[i] = True
        ans.append(string_list[i])
        password(k+1)
        ans.pop()
        for j in range(i+1,C):
            check[j] = False

L, C = map(int,input().split())
string_list = list(input().split())
string_list.sort()
check = [False] * C
ans = []
password(0)