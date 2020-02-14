tc = int(input())
for t in range(tc):
    money = int(input())
    balance = [50000,10000,5000,1000,500,100,50,10]
    balance_list = [0]*len(balance)

    five_man = money//50000
    money = money%50000
    balance_list[0] =five_man

    man = money//10000
    money = money%10000
    balance_list[1] = man

    five_cheon = money//5000
    money = money%5000
    balance_list[2] = five_cheon

    cheon = money//1000
    money = money%1000
    balance_list[3] = cheon

    five_hun = money//500
    money = money%500
    balance_list[4] = five_hun

    hun = money//100
    money = money%100
    balance_list[5] = hun

    five_ten = money//50
    money = money%50
    balance_list[6] = five_ten

    hun = money//10
    money = money%10
    balance_list[7] = hun

    balance_list = [str(_) for _ in balance_list]
    print('#{}'.format(t+1))
    print(' '.join(balance_list))