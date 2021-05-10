n=int(input())
nums=list(map(int,input().split(' ')))
def f(m):
    h=[True for _ in range(m+1)]
    h[1]=False
    for i in range(2,int(m**0.5+1)):
        for j in range(i*2,m+1,i):
            h[j]=False
    return h
m=max(nums)
h=f(m)
cnt=0
for i in nums:
    if h[i]:
        cnt+=1
print(cnt)