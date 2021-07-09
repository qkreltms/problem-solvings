w,h=map(int,input().split())
d=[[] for _ in range(h)]
for i in range(h): 
    d[i]=list(input())
visited=[[False for _ in range(w)] for _ in range(h)]
wPower=0
bPower=0
def bfs(i,j,t):
    q=[(i,j)]
    cnt=0
    while q:
        y,x=q.pop(0)
        if x>=0 and y>=0 and x<w and y<h and not visited[y][x] and d[y][x]==t:
            visited[y][x]=True
            cnt+=1
            q.append((y-1,x))
            q.append((y,x+1))
            q.append((y,x-1))
            q.append((y+1,x))
    return cnt
for i in range(h):
    for j in range(w):
        if not visited[i][j]:
            wPower+=bfs(i,j,'W')**2
            bPower+=bfs(i,j,'B')**2
print(wPower,bPower)
