alphabet = list(map(str,input()))
list1=list()
for x in alphabet:
    list1.append(ord(x)-64)
list1 = [str(n) for n in list1]
print(' '.join(list1))