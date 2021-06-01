v,e=map(int,input().split())
root=[i for i in range(v+1)]
rank=[0 for _ in range(v+1)]
nodes=[]
for _ in range(e):
    a,b,c=map(int,input().split())
    nodes.append((a,b,c))
def find(v):
    if root[v]!=v:
        root[v]=find(root[v])
    return root[v]
def union(m,n):
    if m<n:
        root[m]=n
    else:
        root[n]=m
def f():
    ans=0
    for a,b,c in sorted(nodes, key=lambda x:x[2]):
        r1=find(a)
        r2=find(b)
        if r1 != r2:
            union(r1,r2)
            ans+=c
    return ans
print(f())
