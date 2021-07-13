h,w,n=map(int,input().split())
m=[[0 for _ in range(w)] for _ in range(h)]
visited=[[False for _ in range(w)] for _ in range(h)]
for i in range(n):
    y,x=map(int,input().split())
    m[y-1][x-1]=1
def dfs(y,x):
    cnt=0
    q=[(y,x)]
    while q:
        y,x=q.pop(0)
        if y>=0 and x>=0 and x<w and y<h and visited[y][x]==False and m[y][x]==1:
            visited[y][x]=True
            cnt+=1
            q.append((y-1,x))
            q.append((y,x+1))
            q.append((y,x-1))
            q.append((y+1,x))
    return cnt

ans=0
for y in range(h):
    for x in range(w):
        if visited[y][x]==False:
            ans=max(ans, dfs(y,x))
print(ans)