v,e=map(int,input().split())
h=[]
root=[i for i in range(v+1)]
rank=[0 for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    h.append((a,b,c))
def find(a):
    if root[a]!=a:
        root[a]=find(root[a])
    return root[a]
def union(r1,r2):
    if rank[r1]>rank[r2]:
        root[r2]=r1
    else:
        root[r1]=r2
        if rank[r1]==rank[r2]:
            rank[r2]+=1
ans=0
for a,b,c in sorted(h, key=lambda x: x[2]):
    r1=find(a)
    r2=find(b)
    if r1!=r2:
        union(r1,r2)
        ans+=c
print(ans)