n,k=map(int,input().split())
mul=[0 for _ in range(n)]
plugs=list(map(int,input().split()))
ans=0
for pi, p in enumerate(plugs):
    if p in mul:
        continue
    if 0 in mul:
        mul[mul.index(0)]=p
        continue
    prevTi=0
    target=0
    for mi, m in enumerate(mul):
        if not m in plugs[pi:]:
            target=mi
            break
        ti=plugs[pi:].index(m)
        if ti > prevTi:
            prevTi=ti
            target=mi
    mul[target]=p
    ans+=1
print(ans)
            