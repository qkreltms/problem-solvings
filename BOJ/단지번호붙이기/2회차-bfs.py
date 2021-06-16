n=int(input())
h=[[] for _ in range(n)]
for i in range(n):
    h[i]=list(input())
visited=[[False for _ in range(n)] for _ in range(n)]
ans=[]
def bfs(i,j):
    q=[(i,j)]
    res=0
    while q:
        x,y=q.pop(0)
        if x>=0 and x<n and y>=0 and y<n and not visited[x][y] and h[x][y]=='1':
            res+=1
            visited[x][y]=True
            q.append((x+1,y))
            q.append((x,y+1))
            q.append((x-1,y))
            q.append((x,y-1))
    ans.append(res)
            
for i in range(n):
    for j in range(n):
        if not visited[i][j] and h[i][j]=='1':
            bfs(i,j)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])