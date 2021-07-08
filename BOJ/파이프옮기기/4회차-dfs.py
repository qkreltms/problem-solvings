n=int(input())
h=[[] for _ in range(n)]
for i in range(n):
    h[i]=input().split()
cnt=0
# 1 가로, 2 세로, 3 대각선
def dfs(t,y,x):
    global cnt
    if y==n-1 and x==n-1:
        cnt+=1
        return
    if y<n and x+1<n and h[y][x+1]!='1':
        if t==1 or t==3:
            dfs(1,y,x+1)
    if y+1<n and x<n and h[y+1][x]!='1':
        if t==2 or t==3:
            dfs(2,y+1,x) 
    if y+1<n and x+1<n and h[y][x+1]!='1' and h[y+1][x]!='1' and h[y+1][x+1]!='1':
        if t==1 or t==2 or t==3:
            dfs(3,y+1,x+1)     
dfs(1,0,1)
print(cnt)