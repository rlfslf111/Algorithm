import sys
sys.stdin = open('ladder.txt','r')

dr = [0,0,1]
dc = [-1,1,0]

def dfs():
    for i in range(100):
        if ladder[0][i] == 1: #출발
            visited = [[0]*100 for _ in range(100)]
            visited[0][i] = i
            stack = list()
            stack.append((0,i))
            while len(stack) > 0:
                r, c = stack.pop()
                visited[r][c] = 1
                for k in range(3):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < len(ladder) and 0 <= nc < len(ladder) and visited[nr][nc] == 0:
                        if ladder[nr][nc] == 1:
                            stack.append((nr,nc))
                            break
                        elif ladder[nr][nc] == 2:
                            return i
    return -1

for tc in range(10):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    ans = dfs()
    print('#{} {}'.format(T,ans))