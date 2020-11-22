#문제
'''
이분 그래프인지 판별
이분 그래프란? => 
정점을 집합을 둘로 분할하여, 각 집합에 속한 정점끼리 서로 인접x 일 때 이분그래프
'''
#내 실수
'''
시간초과?!!
'''
#키 포인트
'''
visited를 이용해 색을 입힌다. 예: c=1, f(3-c)를 재귀적으로 순회해 색을 입힘 

n 번째 노드를 선택하고 그 노드와 인접한 정점을 순회할 때 자신과
같은 색이 없다면 이분 그래프
'''
#알게된 것
'''
그래프가 어떤 타입인지 명시 없으면 '무 방향 그래프'
'''
def f():
  stack = [1]
  c = 1
  while stack:
    v = stack.pop()
    if visited[v] == 0:
      c = 3 - c
      visited[v] = c
      stack += adj[v]


t = int(input())
for _ in range(t):
  V, E = map(int, input().split())
  visited = [0 for _ in range(V+1)]
  adj = {}
  for _ in range(E):
    v, e = map(int, input().split())
    if e not in adj:
      adj[e] = [v]
    else: 
      adj[e].append(v)
    if v not in adj:
      adj[v] = [e]
    else:
      adj[v].append(e)
  f()
  #이분 그래프 확인
  ans = 'YES'
  for i in range(1, V+1):
    for j in adj[i]:
      if visited[i] == visited[j]:
        ans = 'NO'
        break
  print(ans)



