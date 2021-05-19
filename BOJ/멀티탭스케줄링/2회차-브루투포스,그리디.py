n,k=list(map(int,input().split()))
plugs=list(map(int,input().split()))
multap=[0 for _ in range(n)]
def f():
    ans=0
    for i,p in enumerate(plugs):
        if p in multap:
            continue
        if 0 in multap:
            multap[multap.index(0)]=p
            continue
        ml,si=0,0
        for j,m in enumerate(multap):
            try:
                mi=plugs[i:].index(m)
                if mi>ml:
                    ml=mi
                    si=j
            except:
                si=j
                break
        multap[si]=p
        ans+=1
    return ans
print(f())