def find_binary(book_page,find_page):
    find_list = [0]*book_page
    find_list[find_page]=1
    initial=1
    count =0
    while True:
        center_page = int((initial+book_page)/2)
        if find_list[center_page]==1:
            break
        if center_page < find_page:
            initial = center_page
        if center_page > find_page:
            book_page = center_page
        count+=1
    return count

test_case = int(input())
for t in range(test_case):
    book_page,A_find,B_find = map(int,input().split())
    count_A = find_binary(book_page,A_find)
    count_B = find_binary(book_page,B_find)
    if count_A < count_B:
        print('#{} {}'.format(t+1,'A'))
    elif count_A > count_B:
        print('#{} {}'.format(t+1,'B'))
    else:
        print('#{} {}'.format(t+1,0))