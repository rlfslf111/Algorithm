for t in range(1,int(input())+1):
    word1, word2 = input().split()
    A, B = len(word1), len(word2)

    lcs = [[0 for i in range(B+1)] for j in range(A+1)]

    for i in range(1, A + 1):
        for j in range(1, B + 1):
            if word1[i-1] == word2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

    print('#{} {}'.format(t,lcs[A][B]))