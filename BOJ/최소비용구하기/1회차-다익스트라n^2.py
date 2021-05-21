import sys
INF=sys.maxsize
n=int(input())
m=int(input())
graph=[[] for _ in range(m+1)]
visited=[False for _ in range(n+1)]
d=[INF for _ in range(n+1)]

for _ in range(m):
    a,b,cost=list(map(int,input().split()))
    graph[a].append((b,cost))
start,end=list(map(int,input().split()))
def getIndex():
    minV=INF
    res=0
    for i in range(1,n+1):
        if not visited[i] and d[i]<minV and i != start:
            minV=d[i]
            res=i
    return res
def f():
    d[start]=0
    visited[start]=True
    for g in graph[start]:
        d[g[0]]=g[1]
 
    for _ in range(n-1):
        stopBy=getIndex()
        if stopBy == 0:
            return
        visited[stopBy]=True
        for g in graph[stopBy]:
            cost=g[1]+d[stopBy]
            if cost<d[g[0]]:
                d[g[0]]=cost
f()
print(d[end])