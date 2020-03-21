def palindrome(word):
    count = 0
    for i in range(len(word)//2):
        if count != 0:
            count -= 1
            continue
        if word[i] == '*':
            count = 19
            continue
        if word[len(word)-1-i] == '*':
            count = 19
            continue
        if word[i] != word[len(word)-1-i]:
            return False
    return True

for t in range(1,int(input())+1):
    word = input()
    if palindrome(word):
        print('#{} Exist'.format(t))
    else:
        print('#{} Not exist'.format(t))