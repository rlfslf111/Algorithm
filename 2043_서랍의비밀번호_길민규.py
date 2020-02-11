def secret(P,K):
    return P-K+1
P,K = map(int,input().split())
print(secret(P,K))