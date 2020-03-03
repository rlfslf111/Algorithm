import sys
sys.stdin = open('input.txt','r')

tc = int(input())
for t in range(tc):
    word = list(input())
    gesu = int(input())
    spot = list(map(int,input().split()))

    spot.sort(reverse=True)
    for i in range(gesu):
        word.insert(spot[i],'-')

    print('#{} {}'.format(t+1,''.join(word)))