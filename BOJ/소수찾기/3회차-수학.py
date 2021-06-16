input()
A=list(map(int,input().split(' ')))
m=max(A)
def f():
    h=[True for _ in range(m+1)]
    h[1]=False
    for i in range(2,int(m**0.5)+1):
        if h[i]:
            for j in range(i*2,m+1,i):
                h[j]=False
    return h
h=f()
cnt=0
for i in A:
    if h[i]:
        cnt+=1
print(cnt)