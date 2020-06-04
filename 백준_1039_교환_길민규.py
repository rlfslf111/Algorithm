from collections import deque
from itertools import combinations
from copy import deepcopy
import sys
inp = sys.stdin.readline


def find():
    compare_list = set()
    ans = 0
    lenq = len(q)
    while lenq:
        v = q.popleft()
        v_list = list(str(v))
        for i, j in ls:
            change = deepcopy(v_list)
            ch_i, ch_j = change[i], change[j]
            change[i], change[j] = ch_j, ch_i
            if change[0] == '0':
                continue
            temp_result = int(''.join(change))
            if temp_result not in compare_list:
                ans = max(ans,temp_result)
                compare_list.add(temp_result)
                q.append(temp_result)
        lenq -= 1
    return ans

N, K = map(int,inp().split())
sample_list = [_ for _ in range(len(str(N)))]
ls = list(combinations(sample_list,2))

q = deque()
q.append(N)

res = 0
while K:
    res = find()
    K -= 1

if res == 0:
    print(-1)
else:
    print(res)