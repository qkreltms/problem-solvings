import heapq
n,e=map(int,input().split())
d=[0 for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
for _ in range(e):
    a,b=map(int, input().split())
    graph[a].append(b)
    d[b]+=1
h,ans=[],[]
for i in range(1,n+1):
    if d[i]==0:
        heapq.heappush(h,i)
while h:
    i=heapq.heappop(h)
    ans.append(i)
    for g in graph[i]:
        d[g]-=1
        if d[g]==0:
            heapq.heappush(h,g)
print(*ans)