# N = 붙이 종이의 갯수, one = 남은 1의 갯수
def attach(N,one):
    if one == 0:
        if N < minv[0]:
            minv[0] = N
    elif N >= minv[0]:
        return
    # 전체가 1로 덮여있을 때 최솟값 4만 출력하고 return
    elif minv[0] == 4:
        return
    elif sum(paper) == 0:
        return
    else:
        for y in range(10):
            for x in range(10):
                # board가 1이고, visit이 0 좌상부터 시작
                if board[y][x] == 1 and visit[y][x] == 0:
                    for p in range(5,0,-1):
                        # 사용할 종이가 남아있고, 범위 내라면,
                        if paper[p] > 0 and y + p <= 10 and x + p <= 10:
                            patch = 0
                            for i in range(y,y+p):
                                for j in range(x, x+p):
                                    if visit[i][j] == 0:
                                        patch += board[i][j]
                            # 덮은 1의 갯수가 종이의 크기와 같으면,
                            if patch == (p*p):
                                for r in range(y, y+p):
                                    for c in range(x, x+p):
                                        visit[r][c] = 1
                                paper[p] -= 1
                                attach(N+1,one - (p*p))
                                # 되돌아가는 자리에 다시 0으로 visit을 돌려준다.
                                for r in range(y, y+p):
                                    for c in range(x, x+p):
                                        visit[r][c] = 0
                                paper[p] += 1
                    # paper의 for문이 모두 돌고나면
                    # (더 이상 종이가 없는 것이 아닌)만족하는 종이가 없는 것이므로
                    # return을 통해서 되돌린다.
                    return

board = [list(map(int,input().split())) for _ in range(10)]
visit = [[0] * 10 for _ in range(10)]
# 1~5(index) 종이 5장씩 준비
paper = [0,5,5,5,5,5]

minv = [(5*5)+1]
one = 0
for y in range(10):
    for x in range(10):
        if board[y][x] == 1:
            one += 1

attach(0,one)
# one == 0으로 모두 덮인 상황이 없는 경우 minv[0] == 26 그대로 함수를 나온다.
if minv[0] == (5*5)+1:
    minv[0] = -1
print(minv[0])