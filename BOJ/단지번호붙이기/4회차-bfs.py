n=int(input())
h=[[] for _ in range(n)]
visited=[[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    h[i]=list(input())
cnt=0
def bfs(i,j):
    q=[(i,j)]
    global cnt
    cnt=0
    while q:
        y,x=q.pop(0)
        if x>=0 and y>=0 and x<n and y<n and h[y][x]=='1' and visited[y][x]==False:
            cnt+=1
            visited[y][x]=True
            q.append((y+1,x))
            q.append((y,x+1))
            q.append((y-1,x))
            q.append((y,x-1))
        
ans=[]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and h[i][j] == '1':
            bfs(i,j)
            ans.append(cnt)
ans.sort()
print(len(ans))
for a in ans:
    print(a)