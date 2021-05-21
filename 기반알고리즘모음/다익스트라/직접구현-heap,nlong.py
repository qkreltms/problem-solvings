import sys
import heapq
n, m = 6, 11
INF = sys.maxsize
startI = 2
d = [INF for _ in range(n+1)]
graph = [
    [],
    [(2, 2), (4, 1), (3, 3)],
    [(4, 2), (3, 3)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    []
]

def f():
  d[startI]=0
  q=[]
  heapq.heappush(0, (0, startI))
  while q:
    cost, pickI=heapq.heappop(q)
    d[pickI]=cost
    for g in graph[pickI]:

