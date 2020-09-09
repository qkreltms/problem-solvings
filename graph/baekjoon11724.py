# 그래프 컴포넌트 개수세기 문제
# 포인트: 이어지는 간선이 없다고 정점이 없는게 아니다. 모든 노드를 루프돈다.

# https://www.acmicpc.net/problem/11724
# 참고 반례
# 1) 
# 999 1
# 1 1
# => 1
# 2)
# 6 2
# 1 3
# 2 3
# 이어지는 간선이 없다고 정점이 없는게 아닙니다
# 그림으로 나타내면...
# 1ㅡ2ㅡ3 4 5 6
# 총 4개네요
import sys

def dfs(start):
  S = [start]

  while S:
    V = S.pop()
    if visited[V] == 0:
      visited[V] = 1
      S += reversed(sorted(list(adj[V])))

# N = 정점의 개수, M = 간선의 개수
N, M = map(int, sys.stdin.readline().split(" "))

adj = [[] for i in range(N+1)]

for _ in range(M):
  n1, n2 = map(int, sys.stdin.readline().split(" "))
  adj[n1].append(n2)
  adj[n2].append(n1)

component = 0
visited = [0] * (N+1)
for i in range(1, N+1):
  if visited[i] == 0:
    dfs(i)
    component +=1
print(component, end="")
