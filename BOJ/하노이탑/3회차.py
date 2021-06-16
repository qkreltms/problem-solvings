def f(n,a,b,c):
    if n == 1:
        print(a,c)
        return
    f(n-1,a,c,b)
    print(a,c)
    f(n-1,b,a,c)
n = int(input())
print(2**n-1)
if n <= 20:
    f(n,1,2,3)