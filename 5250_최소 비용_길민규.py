import math
for k in range(1, int(input())+1):
    N=int(input())
    matrix=[list(map(int,input().split())) for _ in range(N)]

    key=[[math.inf for _ in range(N)] for _ in range(N)]
    key[0][0]=0
    visited=[[False for _ in range(N)] for _ in range(N)]
    checklist=set()
    checklist.add((0,0))
    while(True):

        minimum=math.inf
        min_idx=(-1,-1)
        for i,j in checklist:
                if not visited[i][j] and key[i][j]<minimum:
                    minimum=key[i][j]
                    min_idx=(i,j)
        visited[min_idx[0]][min_idx[1]]=True
        checklist.remove((min_idx))
        if min_idx==(N-1,N-1):
            break
        neighbor=[(0,0)]*4;cnt=0
        for (x,y) in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_x=min_idx[0]+x
                next_y=min_idx[1]+y
                if next_x>=0 and next_x<N and next_y>=0 and next_y<N :
                    neighbor[cnt]=(next_x,next_y);
                    cnt+=1

        for (i,j) in neighbor:
            if not visited[i][j]:
                candidate_value=minimum+1+max(0,matrix[i][j]-matrix[min_idx[0]][min_idx[1]])
                if candidate_value<key[i][j]:
                    checklist.add((i,j))
                    key[i][j]=candidate_value
    print('#{} {}'.format(k,key[N-1][N-1]))