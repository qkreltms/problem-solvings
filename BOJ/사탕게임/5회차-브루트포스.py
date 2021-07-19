n=int(input())
h=[[] for _ in range(n)]
ans=0
for i in range(n):
    h[i]=list(input())
def swap(y,x,isRow):
    if isRow:
        h[y][x],h[y][x+1]=h[y][x+1],h[y][x]
    else:
        h[y][x],h[y+1][x]=h[y+1][x],h[y][x]
def col(x):
    global ans
    w,cnt='',1
    for i in range(n):
        if h[i][x]!=w:
            w=h[i][x]
            ans=max(ans, cnt)
            cnt=1
        else:
            cnt+=1
    ans=max(ans, cnt)
def row(y):
    global ans
    w,cnt='',1
    for i in range(n):
        if h[y][i]!=w:
            w=h[y][i]
            ans=max(ans, cnt)
            cnt=1
        else:
            cnt+=1
    ans=max(ans, cnt)
def search(y,x,isRow):
    swap(y,x,isRow)
    if isRow:
        row(y)
        col(x)
        col(x+1)
    else:
        row(y)
        row(y+1)
        col(x)
    swap(y,x,isRow)
for i in range(n):
    for j in range(n-1):
        search(i,j,True)
for i in range(n-1):
    for j in range(n):
        search(i,j,False)
print(ans)    