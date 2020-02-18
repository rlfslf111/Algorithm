# 1 = 가위, 2 = 바위, 3 = 보

def win(x,y):
    if (card[x-1] == 1 and card[y-1] ==3) or (card[x-1] == 1 and card[y-1] == 1):
        return x
    elif (card[x-1] == 2 and card[y-1] == 1) or (card[x-1] == 2 and card[y-1] == 2):
        return x
    elif (card[x-1] == 3 and card[y-1] == 2) or (card[x-1] == 3 and card[y-1] == 3):
        return x
    return y

def match(start,end):
    if start == end:
        return start
    first = match(start,(start+end)//2)
    second = match((start+end)//2+1, end)
    return win(first,second)

tc = int(input())
for t in range(tc):
    N = int(input())
    card = list(map(int,input().split()))
    start = 1
    end = N
    print('#{} {}'.format(t+1,match(start,end)))