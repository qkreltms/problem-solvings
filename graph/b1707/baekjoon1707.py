# 이분그래프 확인 문제
# 포인트: visited에 1 뿐만 아니라 n 값을 입력해 여러 표시(색)를 할 수 있다는 것을 깨달아야한다.
# 값이 순서대로 주어진다는게 보장된다면 기존에 알고 있는 DFS, BFS 방식을 쓰지 않아도 된다.

# 입력: 
# 첫째 줄 테스트 케이스 개수
# 둘째 줄 그래프의 정점의 개수, 간선의 개수
import sys
sys.setrecursionlimit(999999)
def DFS(v, c):
  visited[v] = c
  for next in adj[v]:
    if visited[next] == 0:
      DFS(next, 3 - c)
  # 키 포인트!!
  # 노드를 돌면서 모든 인접 노드를 순회한다.

  # 마지막으로 아무것도 순회할게 없으면 종료
  return True
    

# 테스트 케이스 개수 (2 <= K <= 5)
T = int(sys.stdin.readline())
for t in range(T):
  # 정점, 간선
  V, E = map(int, sys.stdin.readline().split(" "))
  # 배열 초기화
  adj = [[] for i in range(V+1)]
  # 값 입력
  for i in range(E):
    a, b = map(int, sys.stdin.readline().split(" "))
    adj[a].append(b)
    adj[b].append(a)

  visited = [0] * (V+1)
  for i in range(1, V+1):
    if (visited[i] == 0):
      DFS(i, 1)

  # 이분그래프인지 확인한다.
  isBiGraph = "YES"
  for i in range(1, V+1):
    for j in adj[i]:
      if visited[i] == visited[j]:
        isBiGraph = "NO"
  print(isBiGraph)


