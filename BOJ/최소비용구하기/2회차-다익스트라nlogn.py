import sys
import heapq
n=int(input())
m=int(input())
INF=sys.maxsize
graph=[[] for _ in range(n+1)]
d=[INF for _ in range(n+1)]
for _ in range(m):
    head,to,cost=map(int,input().split())
    graph[head].append((to,cost))
start,end=map(int,input().split())
def f():
    q,d[start]=[],0
    heapq.heappush(q,(0,start))
    while q:
        cost,stopby=heapq.heappop(q)
        if cost>d[stopby]:
            continue
        for i,c in graph[stopby]:
            v=c+cost
            if v<d[i]:
                d[i]=v
                heapq.heappush(q,(v,i))
f()
print(d[end])