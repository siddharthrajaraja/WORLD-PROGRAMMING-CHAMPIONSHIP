v=int(input())
V=[]
while v!=0:
    V.append(int(input()))
    v=v-1

n=int(input())
N=[]
while n!=0:
    
    N.append(int(input()))
    n=n-1

ans=list(set(V).union(set(N)))
c=0
for i in range(0,len(ans)):
    if ans[i]<=1440:
        c=c+1
print(c)

c=0

l=min([len(V),len(N)])    
for i in range(0,l-1):
    if (V[i]>N[i] and V[i+1]<N[i+1]) or  (V[i]<N[i] and V[i+1]>N[i+1]):
        c=c+1
print(c)
