h,w=map(int,input().split())
blocks=list(map(int,input().split()))
def f():
    l,r,lMax,rMax,ans=0,len(blocks)-1,0,0,0
    while l<r:
        if blocks[l] > lMax:
            lMax=blocks[l]
        if blocks[r] > rMax:
            rMax=blocks[r]
        if lMax < rMax:
            ans+=lMax-blocks[l]
            l+=1
        else:
            ans+=rMax-blocks[r]
            r-=1
    return ans
print(f())
        