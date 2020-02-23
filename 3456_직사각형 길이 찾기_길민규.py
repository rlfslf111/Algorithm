tc = int(input())
for t in range(tc):
    square = list(map(int,input().split()))

    one = square[0]
    two = square[1]
    three = square[2]
    if square.count(one) == 1:
        print('#{} {}'.format(t+1,one))
    if square.count(two) == 1:
        print('#{} {}'.format(t+1,two))
    if square.count(three) == 1:
        print('#{} {}'.format(t+1,three))
    if one == two and one == three and two == three:
        print('#{} {}'.format(t+1,one))