def palidrome(word):
    for x in range(len(word)//2):
        if word[x] != word[len(word)-1-x]:
            return 0
        return 1

tc = int(input())
for t in range(tc):
    word = input()
    print('#{} {}'.format(t+1,palidrome(word)))