def palindrome(word):
    for x in range(len(word)//2):
        if word[x] != word[len(word)-1-x]:
            return False
    return True


tc = int(input())
for t in range(tc):
    N, M = map(int,input().split())
    word = [input() for _ in range(N)]

    for y in range(N):
        for x in range(N-M+1):
            count =[]
            for k in range(x,x+M):
                count.append(word[y][k])
            if palindrome(count):
                print('#{} {}'.format(t+1,''.join(count)))

    for x in range(N):
        for y in range(N-M+1):
            count =[]
            for k in range(y,y+M):
                count.append(word[k][x])
            if palindrome(count):
                print('#{} {}'.format(t + 1, ''.join(count)))