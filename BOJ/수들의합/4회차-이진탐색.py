s=int(input())
mid=s//2
end=s
start=0
hap=0
ans=0
while start<=end:
    mid=(start+end)//2
    hap=mid*(mid+1)//2
    if hap>s:
        end=mid-1
    else:
        start=mid+1
        ans=mid
print(ans)