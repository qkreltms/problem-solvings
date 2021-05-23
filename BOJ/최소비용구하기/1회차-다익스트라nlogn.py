import heapq
import sys
INF = sys.maxsize
n = int(input())
m = int(input())
# 주의!: 간선 개수가 n 보다 적을 수 있으므로
# graph의 개수는 n개여야함
graph = [[] for _ in range(n+1)]
d = [INF for _ in range(n+1)]
for _ in range(m):
    head, to, cost = list(map(int, input().split()))
    graph[head].append((to, cost))
start, dest = list(map(int, input().split()))


def f():
    q, d[start] = [], 0
    heapq.heappush(q, (0, start))
    while q:
        cost, head = heapq.heappop(q)
        # 똑같은 노드가 여러번 heap에 저장될 수 있다. 이때
        # 가려는 노드의 값이 이미 최신화된 노드의 값보다 크면 건너뛰고 
        # 최신화된 노드가 다음 노드로 갈 수 있게한다.
        if cost > d[head]:
            continue
        for g in graph[head]:
            x = g[1]+cost
            # cost가 같은 값도 여기서 필터링됨
            if x < d[g[0]]:
                heapq.heappush(q, (x, g[0]))
                d[g[0]] = x


f()
print(d[dest])
