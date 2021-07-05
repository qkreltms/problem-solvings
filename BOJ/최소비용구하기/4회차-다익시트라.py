import heapq
import sys
INF=sys.maxsize
n=int(input())
m=int(input())
d=[INF for _ in range(n+1)]
h=[[] for i in range(n+1)]
for _ in range(m):
    start,end,cost=map(int,input().split())
    h[start].append((cost,end))
start,end=map(int,input().split())
heap=[]
heapq.heappush(heap, (0, start))
while heap:
    t=heapq.heappop(heap)
    for m in h[t[1]]:
        cost=t[0]+m[0]
        if cost<d[m[1]]:
            d[m[1]]=cost
            heapq.heappush(heap,(cost, m[1]))
print(d[end])
    