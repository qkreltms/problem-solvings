a,b=list(map(int,input().split(' ')))
def f():
    x,y=a,b
    while y:
        r=x%y
        x=y
        y=r
    return x
def g(c):
    return int(a*b/c)
r1=f()
r2=g(r1)
print(r1)
print(r2)