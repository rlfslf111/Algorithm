import sys
sys.stdin = open('GNS.txt','r')

dic1 = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
tc = int(input())
for t in range(tc):
    length = input('#{}'.format(t+1)).split()
    word_list = input().split()
    print()

    number = []
    for x in word_list:
        number.append(dic1[x])
    number.sort()

    ans_list = []
    for y in number:
        for x in dic1:
            if dic1[x] == y:
                ans_list.append(x)
    print(' '.join(ans_list))






