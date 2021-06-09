n=int(input())
h=[[] for _ in range(n)]
ans=0
for i in range(n):
    h[i]=list(input())
def swap(i,j,flag):
    if flag:
        if h[i][j] == h[i+1][j]:
            return True
        h[i][j],h[i+1][j]=h[i+1][j],h[i][j]
    else:
        if h[i][j] == h[i][j+1]:
            return True
        h[i][j],h[i][j+1]=h[i][j+1],h[i][j]
def check(i,j,flag):
    global ans
    if swap(i,j,flag):
        return
    for k in range(n):
        w,cnt='',1
        for l in range(n):
            if w!=h[k][l]:
                w=h[k][l]
                ans=max(ans,cnt)
                cnt=1
            else:
                cnt+=1
        ans=max(ans,cnt)
    for k in range(n):
        w,cnt='',1
        for l in range(n):
            if w!=h[l][k]:
                w=h[l][k]
                ans=max(ans,cnt)
                cnt=1
            else:
                cnt+=1
        ans=max(ans,cnt)
    swap(i,j,flag)
def f():
    for i in range(n):
        for j in range(n-1):
            check(j,i,True)
            check(i,j,False)
    return ans
    
print(f())