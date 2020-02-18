for t in range(1,11):
    tc = int(input())
    word = input()
    sentence = input()

    count = 0
    for x in range(len(sentence)-len(word)+1):
        if sentence[x:x+len(word)] == word:
            count +=1

    print('#{} {}'.format(tc,count))