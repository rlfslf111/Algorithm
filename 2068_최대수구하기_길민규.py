def max(number):
    for x in range(len(number)-1):
        for i in range(len(number)-1-x):
            if number[i]>number[i+1]:
                number[i],number[i+1]=number[i+1],number[i]
    return number[-1]
test_case= int(input())
for x in range(test_case):
    number_list = list(map(int,input().split()))
    print('#{} {}'.format(x+1,max(number_list)))