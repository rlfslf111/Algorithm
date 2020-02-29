import sys
sys.stdin = open('pool.txt','r')

def plan(k, sum):
    # 3개월권 때문에 조건을 >= 이상으로
    if k >= 12:
        min_value[0] = min(min_value[0],sum)
    else:
        plan(k+1,sum+(d*table[k]))
        plan(k+1,sum+m)
        plan(k+3,sum+m_3)

tc = int(input())
for t in range(1,tc+1):
    d,m,m_3,y = map(int,input().split())
    table = list(map(int,input().split()))
    #최후의 가격인 1년권과 각 가격을 비교
    min_value = [y]
    #1월부터 읽으면서 비교
    plan(0,0)
    print('#{} {}'.format(t,min_value[0]))