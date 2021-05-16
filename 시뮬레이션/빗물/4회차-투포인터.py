def f():
    l,r,ans,maxL,maxR=0,len(A)-1,0,0,0
    while l<r:
        maxL=max(A[l],maxL)
        maxR=max(A[r],maxR)
        if maxL<=maxR:
            ans+=maxL-A[l]
            l+=1
        else:
            ans+=maxR-A[r]
            r-=1
    return ans
input()
A=list(map(int,input().split(' ')))
print(f()) 
