# 미로탐색 
# BFS를 사용하고, 거리를 카운트해야한다.
# 4방향 순회시 queue에 넣는다.
# 알고리즘 메모리: 31824KB , 속도: 112ms
import collections

h, w = map(int, input().split(' '))

nodes = [0 for _ in range(h)]

for i in range(h):
  nodes[i] = list(map(int, input()))

visited = [[0 for _ in range(w)] for _ in range(h)]

def f(): 
  q = collections.deque()
  q.append([0,0,visited[0][0]])
  while q:
    y, x, v = q.popleft()
    if y >= 0 and x >= 0 and y < h and x < w:
      node = nodes[y][x]
      if visited[y][x] == 0 and node != 0:
        visited[y][x] = v + 1
        q.append([y-1,x, visited[y][x]])
        q.append([y,x+1, visited[y][x]])
        q.append([y+1,x, visited[y][x]])
        q.append([y,x-1, visited[y][x]])


f()
print(visited[h-1][w-1])

