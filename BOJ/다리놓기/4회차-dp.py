t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    h=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==j:
                h[i][j]=1
            elif i==1:
                h[i][j]=j
            else:
                h[i][j]=h[i-1][j-1]+h[i][j-1]
    print(h[i][j])