# m*(m+1)//2
n=int(input())
def f():
    l,r=0,n
    s=0
    ans=0
    while l<=r:
        m=(l+r)//2 
        s=m*(m+1)//2
        if s>n:
            r=m-1
        else:
            l=m+1
            ans=m
    return ans
print(f())