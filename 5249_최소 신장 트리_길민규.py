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
    def get_edge(self,s,t):
        for edge in self.edges:
            if (s==edge[0] and t==edge[1]) or (s==edge[1] and t==edge[0]):
                return edge[2]
    def neighbors(self,obj):
        neighbor=[]
        for edge in self.edges:
            if edge !=None and (edge[0]==obj or edge[1]==obj):
                if edge[0]==obj:
                    neighbor.append((edge[1],edge[2]))
                else:
                    neighbor.append((edge[0],edge[2]))
        return neighbor


for k in range(1, int(input())+1):
    V,E=map(int,input().split())
    g=graph(V+1,E)
    for i in range(E):
        info=list(map(int,input().split()))
        s=info[0];t=info[1];w=info[2]
        g.given_weight(s,t,w)
    key=[math.inf]*(1+V)
    visited=[False]*(1+V)
    pi=[None]*(1+V)
    key[0]=0
    for _ in range(1+V):
        minimum=math.inf
        min_idx=-1
        for i in range(1+V):
            if not visited[i] and key[i]<minimum:
                minimum=key[i]
                min_idx=i
        visited[min_idx]=True
        for (v, val) in g.neighbors(min_idx):
            if not visited[v] and val<key[v]:
                key[v]=val
                pi[v]=min_idx

    print('#{} {}'.format(k,sum(key)))