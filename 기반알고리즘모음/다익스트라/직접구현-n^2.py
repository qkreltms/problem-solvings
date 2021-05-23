'''
'''
import sys
n, m = 6, 11
INF = sys.maxsize
startI = 1
visiteds = [False for _ in range(n+1)]
distances = [INF for _ in range(n+1)]
graphs = [
    [],
    [(2, 2), (4, 1), (3, 3)],
    [(4, 2), (3, 3)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    []
]
# graphs = [
#     [],
#     [(2, INF), (4, INF), (3, INF)],
#     [(4, 2), (3, 3)],
#     [(2, 3), (6, 5)],
#     [(3, 3), (5, 1)],
#     [(3, 1), (6, 2)],
#     []
# ]

def findShortedIndex():
    minV = INF
    minI = 0
    for i in range(1, n+1):
        if not visiteds[i] and distances[i] < minV:
            minV = distances[i]
            minI = i
    return minI


def f():
    visiteds[startI]=True
    distances[startI]=0
    for g in graphs[startI]:
        distances[g[0]] = g[1]
    for _ in range(n-1):
        stopoverI = findShortedIndex()
        # 0이 나왔다는 것은 갈 수 있는 곳이 없다는 것
        if stopoverI == 0:
          return 
        visiteds[stopoverI] = True
        for g in graphs[stopoverI]:
            cost = distances[stopoverI]+g[1]
            if cost < distances[g[0]]:
                distances[g[0]] = cost


f()
for d in distances[1:]:
  print(d if d != INF else 'INF', end=" ")
