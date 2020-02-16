switch_cnt = int(input())
switch = [0] + list(map(int,input().split()))

students = int(input())
for c in range(students):
    sex, number = map(int,input().split())

    if sex == 1:
        for x in range(1,len(switch)):
            if x % number == 0:
                if switch[x] == 0:
                    switch[x] = 1
                elif switch[x] == 1:
                    switch[x] = 0

    if sex == 2:
        if switch[number] == 0:
            switch[number] = 1
        elif switch[number] == 1:
            switch[number] = 0
        i = 1
        while 1:
            if number - i <= 0 or number + i >= len(switch):
                break
            if switch[number-i] != switch[number+i]:
                break
            if switch[number-i] == switch[number+i]:
                if switch[number-i] == 1:
                    switch[number-i] = switch[number+i] = 0
                elif switch[number-i] == 0:
                    switch[number - i] = switch[number + i] = 1
            i += 1

for i in range(1, len(switch), 20):
    if i + 20 < len(switch):
        print(*switch[i:i+20])
    else:
        print(*switch[i:])
