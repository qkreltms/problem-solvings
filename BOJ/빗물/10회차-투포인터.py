h,w=map(int,input().split())
m=list(map(int,input().split()))
lMax,rMax=0,0
l,r=0,len(m)-1
ans=0
while l<r:
    lMax=max(lMax,m[l])
    rMax=max(rMax,m[r])
    if m[l]<m[r]:
        ans+=lMax-m[l]
        l+=1
    else:
        ans+=rMax-m[r]
        r-=1
print(ans)