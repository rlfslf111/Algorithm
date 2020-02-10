tc = int(input())
for t in range(tc):
    card = list(input())
    card_list= [card[i:i+3] for i in range(len(card)) if i%3==0]
    card_SDHC = [13,13,13,13]
    flag = False
    for x in range(len(card_list)-1):
        for y in range(x+1,len(card_list)):
            if card_list[x] == card_list[y]:
                print('#{} ERROR'.format(t+1))
                flag = True
    for x in card_list:
        if x[0] == 'S':
            card_SDHC[0]-=1
        elif x[0] == 'D':
            card_SDHC[1]-=1
        elif x[0] == 'H':
            card_SDHC[2]-=1
        else:
            card_SDHC[3]-=1
    card_SDHC = [str(_) for _ in card_SDHC]
    if not flag:
        print('#{} {}'.format(t+1,' '.join(card_SDHC)))
