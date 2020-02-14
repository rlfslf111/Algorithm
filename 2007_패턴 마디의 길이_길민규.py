tc = int(input())
for t in range(tc):
    word = list(input())
    count = 1
    for x in range(len(word)):
        if word[0:2] == word[1+x:3+x]:
            break
        count+=1
    print('#{} {}'.format(t+1,count))