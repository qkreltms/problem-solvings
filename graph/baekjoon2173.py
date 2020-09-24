# 미로탐색 
# BFS를 사용하고, 거리를 카운트해야한다.
import collections

w, h = map(int, input().split(' '))

nodes = [0 for _ in range(h)]

for _ in range(h):
  nodes = map(int, input().split(' '))

visited = [ False [for _ in range(w)] for _ in range(h)]

def y(y, x): 

Q = collections.deque()
for y in range(h):
  for x in range(w):
    f(y, x)

