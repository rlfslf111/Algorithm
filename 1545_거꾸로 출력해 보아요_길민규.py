su = int(input())
list1 = list()
for x in range(su,-1,-1):
    list1.append(x)
list1 = [str(_) for _ in list1]
print(' '.join(list1))