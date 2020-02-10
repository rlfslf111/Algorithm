def y_m_d(ymd):
    year_month_date = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    year = ymd[0:4]
    month = ymd[4:6]
    date = ymd[6:]
    for i in year_month_date:
        if int(month) < 1 or int(month) > 12:
            return -1
        if int(month) == i:
            if int(date) > year_month_date[i]:
                return -1
    else:
        return year+'/'+month+'/'+date
test_case = int(input())
for x in range(test_case):
    ymd = input()
    print('#{} {}'.format(x+1,y_m_d(ymd)))