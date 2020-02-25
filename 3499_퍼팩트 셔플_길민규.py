tc = int(input())
for t in range(tc):
    deck = int(input())
    word = list(input().split())

    first_deck = []
    second_deck = []
    if deck % 2 == 0:
        for x in range(0,deck//2):
            first_deck.append(word[x])
        for y in range(deck//2,deck):
            second_deck.append(word[y])
    else:
        for x in range(0,deck//2+1):
            first_deck.append(word[x])
        for y in range(deck//2+1,deck):
            second_deck.append(word[y])

    ans = []
    if len(first_deck) == len(second_deck):
        for i in range(len(first_deck)):
            ans.append(first_deck[i])
            ans.append(second_deck[i])
    else:
        for i in range(len(second_deck)):
            ans.append(first_deck[i])
            ans.append(second_deck[i])
        else:
            ans.append(first_deck[-1])
    print('#{} {}'.format(t+1,' '.join(ans)))