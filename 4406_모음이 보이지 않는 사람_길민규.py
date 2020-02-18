vowel = 'aeiou'

tc = int(input())
for t in range(tc):
        word = input()
        execpt = []
        for x in range(len(word)):
            if word[x] in vowel:
                continue
            else:
                execpt.append(word[x])
        print('#{} {}'.format(t+1,''.join(execpt)))