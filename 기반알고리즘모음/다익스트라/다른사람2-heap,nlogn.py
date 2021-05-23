import heapq
import sys
INF = int(1e9)  #무한을 의미하는 값으로 10억을 설정.
n, m = 6, 11
INF = sys.maxsize
start = 1
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

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    d[start] = 0
    while q:    #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        #heap은 기본적으로 min heap
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if d[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    #도달할 수 없는 경우, 무한이라고 출력
    if d[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리를 출력
    else:
        print(d[i])