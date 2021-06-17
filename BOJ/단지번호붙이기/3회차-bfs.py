n=int(input())
h=[[] for _ in range(n)]
visited=[[False for _ in range(n)] for _ in range(n)] 
for i in range(n):
    h[i]=list(input())
ans=[]
def bfs(i,j):
    q=[(i,j)]
    cnt=0
    while q:
        x,y=q.pop(0)
        if x>=0 and y>=0 and x<n and y<n and h[x][y]=='1' and not visited[x][y]:
            visited[x][y]=True
            cnt+=1
            q.append((x+1,y))
            q.append((x,y+1))
            q.append((x-1,y))
            q.append((x,y-1))
    ans.append(cnt)
for i in range(n):
    for j in range(n):
        if not visited[i][j] and h[i][j]=='1':
            bfs(i,j)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])