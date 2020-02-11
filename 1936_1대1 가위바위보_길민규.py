def rock(a,b):
    if a == 1 and b == 3:
        return 'A'
    elif a == 1 and b == 2:
        return 'B'
    elif a == 2 and b == 1:
        return 'A'
    elif a == 2 and b == 3:
        return 'B'
    elif a ==3 and b == 1:
        return 'B'
    else:
        return 'A'
a,b = map(int,input().split())
print(rock(a,b))