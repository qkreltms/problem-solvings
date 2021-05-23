import sys
import heapq
n, m = 6, 11
INF = sys.maxsize
startI = 1
d = [INF for _ in range(n+1)]
graph = [
    [],
    [(2, 2), (4, 1), (3, 3)],
    [(4, 2), (3, 3)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)]
]


def f():
    q = []
    d[startI] = 0
    heapq.heappush(q, (0, startI))
    while q:
        cost, pickI = heapq.heappop(q)
        # 똑같은 노드가 여러번 heap에 저장될 수 있다. 이때
        # 가려는 노드의 값이 이미 최신화된 노드의 값보다 크면 건너뛰고 
        # 최신화된 노드가 다음 노드로 갈 수 있게한다.
        if cost > d[pickI]:
            continue
        for g in graph[pickI]:
            x = g[1]+cost
            if x < d[g[0]]:
                d[g[0]] = x
                heapq.heappush(q, (x, g[0]))
f()
for i in d[1:]:
  print(i if i != INF else 'INF', end=' ')
