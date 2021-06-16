a,b=map(int,input().split())
def f(x,y):
    r=1
    while r!=0:
        r=x%y
        x=y
        y=r
    return x
x=f(a,b)
y=int(a*b/x)
print(x)
print(y)