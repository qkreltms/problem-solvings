n,k=map(int,input().split())
si,ei,ans=-1,0,100000001
tList=list(map(int, input().split()))
s=tList[0]
while True:
    if s>=k:
        si+=1
        s-=tList[si]
        ans=min(ans,ei-si+1)
        if ans==1:
            break
    elif ei>=n-1:
        break
    elif s<k:
        ei+=1
        s+=tList[ei]
print(0 if ans == 100000001 else ans)