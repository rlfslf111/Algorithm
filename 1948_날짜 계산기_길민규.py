def month_date_cal(month_date):
    month_and_date = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    first_date_initial = 0
    second_date_initial = 0
    for x in month_and_date:
        first_date_initial += month_and_date[x]
        if month_date[0] < x+2:
            break
    first_date_initial+=month_date[1]
    for x in month_and_date:
        second_date_initial += month_and_date[x]
        if month_date[2] < x+2:
            break
    second_date_initial+=month_date[3]
    if month_date[0]==1:
        first_date_initial=month_date[1]
    return second_date_initial-first_date_initial+1

test_case = int(input())
for x in range(test_case):
    month_date = list(map(int,input().split()))
    print('#{} {}'.format(x+1,month_date_cal(month_date)))