import heapq
import sys
INF=sys.maxsize
cityNum=int(input())
busNum=int(input())
g=[[] for _ in range(cityNum+1)]
d=[INF for _ in range(cityNum+1)]
for _ in range(busNum):
    a,b,cost=map(int,input().split())
    g[a].append((cost,b))
start,end=map(int,input().split())
def f():
    h=[]
    heapq.heappush(h,(0,start))
    while h:
        targetCost,targetIndex=heapq.heappop(h)
        for cost,to in g[targetIndex]:
            v=cost+targetCost
            if v < d[to]:
                heapq.heappush(h,(v,to))
                d[to]=v
f()
print(d[end])