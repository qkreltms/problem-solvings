# 입력: 
# 첫째 줄 테스트 케이스 개수
# 둘째 줄 그래프의 정점의 개수, 간선의 개수
import sys
sys.setrecursionlimit(999999)
def DFS(v, c):
  visited[v] = c
  for next in adj[v]:
    if visited[next] == 0:
      if DFS(next, 3 - c) == False:
        # 다음 노드가 현재와 색이 같다면 종료시킨다.
        return False

    elif visited[next] == visited[v]:
      return False
  # 1 - 2, 1 - 3과 같은 구조일 때 1 -> 2, 2 -> 1 갈 때 방문한 노드지만 색이 같지 
  # 않으므로 True 반환 그렇게 해서 계속 for문 타서 1 -> 3도 갈 수 있도록 함
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


