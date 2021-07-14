def f(x):
    if len(x)<=1:
        return x
    mid=x[len(x)//2]
    l=[]
    r=[]
    equal=[]
    for i in x:
        if i > mid:
            r.append(i)
        elif i < mid:
            l.append(i)
        else:
            equal.append(i)
    return f(l)+equal+f(r)
print(f([6,5,4,1,32,4,2,4]))

