n=int(input())
def f(k,a,b,c):
    if k==1:
        print(a,c)
        return
    f(k-1,a,c,b)
    print(a,c)
    f(k-1,b,a,c)
print(2**n-1)
if n<=20:
    f(n,1,2,3)

