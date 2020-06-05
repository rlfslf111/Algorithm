import sys
input = sys.stdin.readline

from itertools import product
from copy import deepcopy

def game(case):
    # 5번 움직이기
    for i in case:
        # 위로 합치기 and 밀기
        if i == 0:
            for x in range(N):
                for y in range(N-1):
                    if board[y][x] != 0:
                        for k in range(y+1,N):
                            if board[k][x] != 0:
                                if board[k][x] == board[y][x]:
                                    board[y][x] *= 2
                                    board[k][x] = 0
                                break
            for x in range(N):
                for y in range(N-1):
                    if board[y][x] == 0:
                        for k in range(y+1,N):
                            if board[k][x] != 0:
                                board[y][x] = board[k][x]
                                board[k][x] = 0
                                break
        # 오른쪽 합치기 and 밀기
        if i == 1:
            for y in range(N):
                for x in range(N-1,0,-1):
                    if board[y][x] != 0:
                        for k in range(x-1,-1,-1):
                            if board[y][k] != 0:
                                if board[y][x] == board[y][k]:
                                    board[y][x] *= 2
                                    board[y][k] = 0
                                break
            for y in range(N):
                for x in range(N-1,0,-1):
                    if board[y][x] == 0:
                        for k in range(x-1,-1,-1):
                            if board[y][k] != 0:
                                board[y][x] = board[y][k]
                                board[y][k] = 0
                                break
        # 아래로 합치기 and 밀기
        if i == 2:
            for x in range(N):
                for y in range(N-1,0,-1):
                    if board[y][x] != 0:
                        for k in range(y-1,-1,-1):
                            if board[k][x] != 0:
                                if board[k][x] == board[y][x]:
                                    board[y][x] *= 2
                                    board[k][x] = 0
                                break
            for x in range(N):
                for y in range(N-1,0,-1):
                    if board[y][x] == 0:
                        for k in range(y-1,-1,-1):
                            if board[k][x] != 0:
                                board[y][x] = board[k][x]
                                board[k][x] = 0
                                break
        # 왼쪽 합치기 and 밀기
        if i == 3:
            for y in range(N):
                for x in range(N-1):
                    if board[y][x] != 0:
                        for k in range(x+1,N):
                            if board[y][k] != 0:
                                if board[y][k] == board[y][x]:
                                    board[y][x] *= 2
                                    board[y][k] = 0
                                break
            for y in range(N):
                for x in range(N-1):
                    if board[y][x] == 0:
                        for k in range(x+1,N):
                            if board[y][k] != 0:
                                board[y][x] = board[y][k]
                                board[y][k] = 0
                                break

    for i in range(N):
        for j in range(N):
            maxv[0] = max(maxv[0],board[i][j])

N = int(input())
initial = [list(map(int,input().strip().split())) for _ in range(N)]
board = deepcopy(initial)

maxv = [0]

# 0,1,2,3 (상,우,하,좌) 방향으로 이동
dir = list(range(4))
# 4개의 방향을 5번 움직이는 모든 경우의 수 1024개
for i in product(dir,repeat=5):
    game(i)
    board = deepcopy(initial)
print(maxv[0])