su = int(input())
su_list = [2**x for x in range(su+1)]
su_list = [str(_) for _ in su_list]
print(' '.join(su_list))