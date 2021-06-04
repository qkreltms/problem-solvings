import heapq
n,m=map(int,input().split())
d=[0 for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    d[b]+=1
q=[]
res=[]
for i in range(1, n+1):
    if d[i]==0:
        heapq.heappush(q,i)
while q:
    t=heapq.heappop(q)
    res.append(t)
    for g in graph[t]:
        d[g]-=1
        if d[g]==0:
            heapq.heappush(q,g)
print(*res)