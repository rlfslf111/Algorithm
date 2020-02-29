def virus(visit,V):
    for i in range(1,N+1):
        if network[V][i] == 1 and i not in visit:
            visit.append(i)
            virus(visit,i)
    return visit
N = int(input())
E = int(input())
network = [[0]*(N+1) for _ in range(N+1)]
for e in range(E):
    com1, com2 = map(int,input().split())
    network[com1][com2] = network[com2][com1] = 1

print(len(virus([1],1))-1)
