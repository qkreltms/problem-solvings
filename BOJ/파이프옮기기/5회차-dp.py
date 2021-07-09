n=int(input())
h=[[] for _ in range(n)]
for i in range(n):
    h[i]=input().split()
d=[[[0,0,0] for _ in range(n)] for _ in range(n)]
d[0][1][0]=1
for i,_ in enumerate(d[0][2:]):
    if h[0][i+2]=='1':
        continue
    d[0][i+2][0]=1
for i in range(1,n):
    for j in range(1,n):
        if h[i][j]=='1':
            continue
        d[i][j][0]=d[i][j-1][2]+d[i][j-1][0]
        d[i][j][1]=d[i-1][j][2]+d[i-1][j][1]
        if h[i-1][j]=='1' or h[i][j-1]=='1':
            continue
        d[i][j][2]=d[i-1][j-1][2]+d[i-1][j-1][1]+d[i-1][j-1][0]
print(sum(d[n-1][n-1]))