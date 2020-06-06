# https://www.acmicpc.net/problem/1260
import collections

def dfs(V):
    result = []
    S = [V]
    visited = [0] * (N+1)
    while S:
        V = S.pop()
        # 한번도 방문하지 않았을 때
        if visited[V] == 0:
            visited[V] = 1
            result.append(V)
            S += reversed(sorted(list(adj[V])))

    return result


def bfs(V):
    result = []
    Q = collections.deque([V])
    visited = [0] * (N+1)
    while Q:
        V = Q.popleft()
        # 한번도 방문하지 않았을 때
        if visited[V] == 0:
            visited[V] = 1
            result.append(V)
            for i in sorted(list(adj[V])):
                Q.append(i)

    return result

# N = 정점, M = 간선, V = start node name
N, M, V = map(int, input().split(" "))
# 인접리스트 (2차원 배열)
# 1부터 이므로 + 1을 해준다. 
adj = [set() for _ in range(N+1)]
for i in range(M):
    n1, n2 = map(int, input().split(" "))
    adj[n1].add(n2)
    adj[n2].add(n1)

print(*dfs(V))
print(*bfs(V))
