def f(a,b):
    while b:
        r=a%b
        a=b
        b=r
    return a
def f2(g):
    global a,b
    return int(a*b/g)
a,b=list(map(int,input().split(' ')))
g=f(a,b)
print(g)
print(f2(g))