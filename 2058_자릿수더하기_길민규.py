def jarisu_sum(num):
    num_str = str(num)
    sum=0
    num_str = [int(_) for _ in num_str]
    for x in num_str:
        sum+=x
    return sum
su = int(input())
print(jarisu_sum(su))