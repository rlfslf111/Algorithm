def factorization(number):
    count_list=[0]*5
    while number%2==0:
        number = number//2
        count_list[0]+=1
    while number%3==0:
        number = number//3
        count_list[1]+=1
    while number%5==0:
        number = number//5
        count_list[2]+=1
    while number%7 == 0:
        number = number//7
        count_list[3]+=1
    while number%11 == 0:
        number = number//11
        count_list[4]+=1
    count_list = [str(_) for _ in count_list]
    return ' '.join(count_list)
test_case = int(input())
for x in range(test_case):
    number = int(input())
    print('#{} {}'.format(x+1,factorization(number)))