# N, K = map(int,input().split())
# count = 0

n,k = map(int,input().split())
cnt =0

def bfs(n,k,cnt):
    con =1
    visited = set()
    location = set()
    location.add(n)
    while(con):
        if(k in location):
            con =0
            return cnt
        else:
            cnt+=1
            temp=list()
            while(location):
                temp_loc =location.pop()
                temp.append(temp_loc)
                visited.add(temp_loc)
            for i in range(len(temp)):
                if(temp[i]+1 not in visited):
                    if(temp[i]+1<=100000):
                        location.add(temp[i]+1)
                if(temp[i]-1 not in visited):
                    if(temp[i]-1>=0):
                        location.add(temp[i]-1)
                if(temp[i]*2 not in visited):
                    if(temp[i]*2<=100000):
                        location.add(temp[i]*2)

cnt = bfs(n,k,cnt)
print(cnt)
