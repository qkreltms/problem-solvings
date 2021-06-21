h,w=map(int, input().split())
heights=list(map(int, input().split()))
l,r=0,w-1
lMax,rMax=heights[l],heights[r]
ans=0
while l < r:
    rMax=max(rMax,heights[r])
    lMax=max(lMax,heights[l])
    if lMax > rMax:
        ans+=rMax-heights[r]
        r-=1
    else:
        ans+=lMax-heights[l]
        l+=1
print(ans)
        