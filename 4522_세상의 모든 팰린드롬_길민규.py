def palindrome(word):
    for i in range(len(word)//2):
        if word[i] == '?':
            continue
        if word[len(word)-1-i] == '?':
            continue
        if word[i] != word[len(word)-1-i]:
            return False
    return True

tc = int(input())
for t in range(1,tc+1):
    word = list(input())


    if palindrome(word):
        print('#{} {}'.format(t,'Exist'))
    else:
        print('#{} {}'.format(t,'Not exist'))
