# def paper(width):
#     if width == 0 or width == 1:
#         return 1
#     return paper(width-2)*2 + paper(width-1)
#
# tc = int(input())
# for t in range(tc):
#     width = int(input())
#     width = width//10
#     print('#{} {}'.format(t+1,paper(width)))

def get_sum(x):
    if x == N:
        return 1
    if x > N:
        return 0
    return get_sum(x+10) + get_sum(x+20) * 2

T = int(input())
for tc in range(T):
    N = int(input())
    print('#{} {}'.format(tc,get_sum(0)))
