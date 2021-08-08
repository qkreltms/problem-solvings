s=int(input())
l,r=0,s
ans=0
while l<=r:
    mid=(l+r)//2
    hap=mid*(mid+1)//2
    if hap>s:
        r=mid-1
    else:
        l=mid+1
        ans=mid
print(ans)
    
