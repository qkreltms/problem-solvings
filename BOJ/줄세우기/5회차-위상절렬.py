# heap 필요없음, 왜냐하면 어차피 d[n] 값이 0인 값만 담는데 왜 필요한가? (모두 0 인값을 왜 대소비교?)
n,m=map(int,input().split())
d=[0 for _ in range(n+1)]
d[0]=1
g=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    d[b]+=1
h=[]
for i,c in enumerate(d):
    if c==0:
        h.append(i)
ans=[]
while h:
    i=h.pop(0)
    ans.append(i)
    for c in g[i]:
        d[c]-=1
        if d[c]==0:
            h.append(c)
print(*ans)