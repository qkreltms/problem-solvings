#문제
'''
방향 없는 그래프 일 때
연결 요소 개수는?

첫 줄에 정점(N), 간선(M)의 개수가 주어지고
그 다음부터 간선의 양 끝점이 주어진다.
'''
#내 실수
'''
'연결 요소'라는 단어의 정의를 잘 알지 못 했다.
연결 그래프 = 연결 요소,
연결 그래프는 모든 두 꼭짓점 사이에 경로가 존재하는 그래프
방향이 없는 그래프는 꼭지점 간에 구별이 없으므로 예외 사항(?)
즉, 이 문제에서 1개 짜리도 연결 요소라고 친다.
'''
#포인트
'''
포인트: 이어지는 간선이 없다고 정점이 없는게 아니다.
'''
# https://www.acmicpc.net/problem/11724

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

# 참고 반례
# 1) 
# 999 1
# 1 1
# 999
# 2)
# 6 2
# 1 3
# 2 3
# 이어지는 간선이 없다고 정점이 없는게 아닙니다
# 그림으로 나타내면...
# 1ㅡ2ㅡ3 4 5 6
# 총 4개네요
