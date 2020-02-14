import sys
sys.stdin = open('baek.txt','r')

tc = int(input())
for t in range(tc):
    date = int(input())
    date_price = list(map(int,input().split()))

    max_price_idx = date_price.index(max(date_price))
    count = 0
    buy = 0
    for x in range(0,max_price_idx):
        count += 1
        buy += date_price[x]
    max_price = date_price[max_price_idx] * count

    benefit = max_price - buy
    print(benefit)

