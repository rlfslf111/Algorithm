def runwin(player):
    for i in range(len(player)-2):
        if player[i] and player[i+1] and player[i+2]:
            return True
    return False

def triplet(player):
    if 3 in player:
        return True
    return False

for t in range(1,int(input())+1):
    card = list(map(int,input().split()))
    play1 = [0] * 10
    play2 = [0] * 10
    flag = False
    for i in range(0,len(card),2):
        play1[card[i]] += 1
        play2[card[i+1]] += 1
        if runwin(play1):
            print('#{} {}'.format(t,1))
            flag = True
            break
        if triplet(play1):
            print('#{} {}'.format(t,1))
            flag = True
            break
        if runwin(play2):
            print('#{} {}'.format(t,2))
            flag = True
            break
        if triplet(play2):
            print('#{} {}'.format(t,2))
            flag = True
            break
    if not flag:
        print('#{} {}'.format(t,0))