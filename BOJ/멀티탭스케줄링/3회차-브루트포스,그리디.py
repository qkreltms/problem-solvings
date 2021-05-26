n,k=map(int,input().split())
plugs=list(map(int, input().split()))
mul=[0 for _ in range(n)]
def f():
    ans=0
    if k == 1 and n == 1:
        return 0
    for i,p in enumerate(plugs):
        if p in mul:
            continue
        if 0 in mul:
            mul[mul.index(0)]=p
            continue
        t=0
        xl=0
        for j,m in enumerate(mul):
            if m in plugs[i:]:
              x=plugs[i:].index(m)
              if x > xl:
                xl=x
                t=j
            else:
                t=j
                break
        mul[t]=p
        ans+=1
    return ans
print(f())