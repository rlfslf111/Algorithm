from copy import deepcopy

dy = [-1,0,0]
dx = [0,-1,1]
def attack(arr):
    enemy = deepcopy(fight)
    kill = 0
    x1, x2, x3 = arr

    while 1:
        zero = 0
        for z in range(N):
            zero += enemy[z].count(0)
        if zero == N*M:
            break

        # 범위 내에 있는 적을 죽이기
        delete1 = []
        delete2 = []
        delete3 = []
        # 거리내에 있는 적부터
        for d in range(1,D+1):
            for i in range(M):
                for j in range(N-1,-1,-1):
                    if (abs(N-j) + abs(x1-i)) == d:
                        if enemy[j][i] == 1:
                            delete1.append((j,i))
                    if (abs(N-j) + abs(x2-i)) == d:
                        if enemy[j][i] == 1:
                            delete2.append((j,i))
                    if (abs(N-j) + abs(x3-i)) == d:
                        if enemy[j][i] == 1:
                            delete3.append((j,i))

        # 만족하는 거리에 적이 없을 경우가 있으므로
        if len(delete1) > 0:
            enemy[delete1[0][0]][delete1[0][1]] = 3
        if len(delete2) > 0:
            enemy[delete2[0][0]][delete2[0][1]] = 3
        if len(delete3) > 0:
            enemy[delete3[0][0]][delete3[0][1]] = 3

        for i in range(N):
            for j in range(M):
                if enemy[i][j] == 3:
                    kill += 1
                    enemy[i][j] = 0

        # 제외할 적을 제외하고 한 칸씩 당기기
        enemy[N-1] = [0]*M
        for y in range(N-1,0,-1):
            for x in range(M):
                enemy[y][x] = enemy[y-1][x]
        enemy[0] = [0] * M

    return kill

def perm(k):
    if k == 3:
        maxv[0] = max(attack(arr),maxv[0])
        return
    else:
        for i in range(M):
            if not check[i]:
                check[i] = True
                arr.append(num[i])
                perm(k+1)
                arr.pop()
                for j in range(i+1,M):
                    check[j] = False

N, M, D = map(int,input().split())
enemy = [list(map(int,input().split())) for _ in range(N)]
fight = deepcopy(enemy)

check = [False] * M
num = list(range(M))
arr = []
maxv = [0]
perm(0)
print(maxv[0])