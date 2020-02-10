tc = int(input())
for t in range(tc):
    word = input()
    check = input()
    count = 0
    for x in range(0,len(check)):
        if check[x:x+len(word)] == word:
            count += 1
    print('#{} {}'.format(t+1,count))