def f():
    ans=0
    for i in range(w):
        x=min(max(A[:i] or [0]), max(A[i:] or [0]))-A[i]
        if x>0:
            ans+=x
    return ans
h,w=list(map(int,input().split(' ')))
A=list(map(int,input().split(' ')))
print(f())  
