T=int(input())

for asd in range(T):
    N = int(input())
    price=list(map(int,input().split()))

    ans1=[]
    ans2=[]
    # 아이디어
    # 뒤에서부터 순회하면서 자신보다 작은 녀석은 수익을 낸다.
    # max 보다 더 큰 숫자가 나올 때까지, 수익 책정
    earn = 0 #수익을 저장할 배열
    max_price = price[N-1]
    for i in range(N-2,-1,-1):
        if price[i]<max_price:
            earn+=max_price-price[i]
            #최고가 - 현재 가격을 수익으로 더한다.
        else:
            max_price=price[i]
    print('#{} {}'.format(asd+1,earn))




# tc = int(input())
# for t in range(tc):
#     buy = int(input())
#     price = list(map(int,input().split()))
#
#     sum_list = []
#     max = 0
#     for x in range(len(price)-1,-1,-1):
#         if price[x] > max:
#             max = price[x]
#         if price[x] < max:
#             sum_list.append(max - price[x])
#
#     sum = 0
#     for x in sum_list:
#         sum += x
#     if len(sum_list) == 0:
#         print('#{} {}'.format(t+1,0))
#     else:
#         print('#{} {}'.format(t+1,sum))



