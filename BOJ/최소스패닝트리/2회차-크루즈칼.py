# 최적화 기법 2가지 쓰임, rank, 흔적 담아서 e-1개만 수행하기
v,e=map(int,input().split())
edges=[]
roots=[i for i in range(v+1)]
ranks=[0 for _ in range(v+1)]
for _ in range(e):
    x,y,c=map(int,input().split())
    edges.append((x,y,c))
def find(x):
    if roots[x] != x:
        roots[x] = find(roots[x])
    return roots[x]
def union(r1,r2):
    if ranks[r1] > ranks[r2]:
        roots[r2]=r1
    else:
        roots[r1]=r2
        if ranks[r1] == ranks[r2]:
            ranks[r2]+=1
prevs=[]
def f():
    ans=0
    for x,y,c in sorted(edges, key=lambda x:x[2]):
        r1=find(x)
        r2=find(y)
        if r1 != r2:
            union(r1,r2)
            ans+=c
            prevs.append((r1,r2))
            if len(prevs) == e-1:
                break
    return ans
print(f())