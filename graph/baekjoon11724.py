# https://www.acmicpc.net/problem/11724

def dfs(start):
  S = [start]
  visited = [0] * (N+1)

  while S:
    V = S.pop()
    if visited[V] == 0:
      visited[V] = 1
      S += reversed(sorted(list(adj[V])))
      del adj[V]

# N = 정점의 개수, M = 간선의 개수
N, M = map(int, input().split(" "))

adj = {i: set() for i in range(N+1)}

for _ in range(M):
  n1, n2 = map(int, input().split(" "))
  adj[n1].add(n2)
  adj[n2].add(n1)

component = 0
while adj:
  key = list(adj.keys())[0]
  # 값이 아무것도 없을 때는 실행하지 않는다.
  if len(adj[key]) == 0: 
    del adj[key]
    continue
  dfs(key)
  component +=1
print(component, end="")
