n=int(input())
start,end,ans=1,n,0
while start<=end:
    mid=(start+end)//2
    s=mid*(mid+1)//2
    if s>n:
        end=mid-1
    else:
        start=mid+1
        ans=mid
print(ans)
        