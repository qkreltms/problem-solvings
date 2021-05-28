import sys
n,s=map(int,input().split())
arr=list(map(int,input().split()))
def f():
    ans=sys.maxsize
    hap=0
    l,r=0,0
    while True:
        if hap>=s:
            ans=min(ans,r-l)
            hap-=arr[l]
            l+=1
            if l==r:
                return 1
        elif r>=n:
            break
        else:
            hap+=arr[r]
            r+=1
    if ans==sys.maxsize:
        return 0
    return ans
print(f())
        
        