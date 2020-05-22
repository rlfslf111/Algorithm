import math
class graph:
    def __init__(self,V,E):
        self.nodes=[i for i in range(V)]
        self.edges=[None]*E
        self.idx=0
    def given_weight(self,s,t,w):
        idx=self.idx
        self.edges[idx]=(s,t,w)
        self.idx+=1

    def neighbors(self,obj):
        neighbor=[]
        for edge in self.edges:
            if edge !=None and edge[0]==obj :
                neighbor.append((edge[1],edge[2]))
        return neighbor
for k in range(1, int(input())+1):
    N,E=map(int,input().split())
    g=graph(N+1,E)
    for _ in range(E):
        info=list(map(int,input().split()))
        g.given_weight(*info)

    key=[math.inf]*(N+1)
    key[0]=0
    visited=[False for _ in range(N+1)]
    checklist=set()
    checklist.add((0))

    while(True):
        minimum=math.inf
        min_idx=None
        for i in checklist:
                if not visited[i] and key[i]<minimum:
                    minimum=key[i]
                    min_idx=i
        visited[min_idx]=True
        checklist.remove(min_idx)
        if min_idx==(N):
            break
        neighbor=g.neighbors(min_idx)
        for (t,w) in neighbor:
                if not visited[t] and w+key[min_idx]<key[t]:
                    checklist.add(t)
                    key[t]=w+key[min_idx]

    print('#{} {}'.format(k,key[N]))