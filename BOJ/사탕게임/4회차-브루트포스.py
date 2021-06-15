n=int(input())
h=[[] for _ in range(n)]
ans=0
for i in range(n):
    h[i]=list(input())
def swap(i,j,flag):
    if flag:
        h[i][j+1],h[i][j]=h[i][j],h[i][j+1]
    else:
        h[j][i],h[j+1][i]=h[j+1][i],h[j][i]
def row(i):
    global ans
    w,cnt='',0
    for j in range(n):
        if w!=h[i][j]:
            w=h[i][j]
            ans=max(cnt,ans)
            cnt=1
        else:
            cnt+=1
    ans=max(cnt,ans)
def col(i):
    global ans
    w,cnt='',0
    for j in range(n):
        if w!=h[j][i]:
            w=h[j][i]
            ans=max(cnt,ans)
            cnt=1
        else:
            cnt+=1
    ans=max(cnt,ans)
def check(flag):
    for i in range(n):
        for j in range(n-1):
            swap(i,j,flag)
            if flag:
                row(i)
                col(j)
                col(j+1)
            else:
                row(j)
                row(j+1)
                col(i)
            swap(i,j,flag)
check(True)
check(False)
print(ans)