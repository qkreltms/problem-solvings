#내 실수
'''
1. sys.stdin.readline()를 쓰면 읽기 속도가 압도적으로 빨라지는걸 인지하지 못 했다.
2. 일차원 배열로 nodes를 사용했다. 
이 경우 1 5, 4 1이 들어올 경우 방향있는 그래프처럼 되므로 틀린방법이다. 
'''
#잘 한점
'''
1. 이전에 stack에 배열을 합칠 때 정렬을 했는데 
정렬이 필요없다는 것을 알았다 왜냐면 어디로 가든 상관없고 순회만 잘 하면 되니까
(but 빨리진 속도는 미미하다...)
'''
import sys

# N = 정점의 개수, M = 간선의 개수
N, M = map(int, sys.stdin.readline().split())
nodes = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
  v1, v2 = map(int, sys.stdin.readline().split())
  nodes[v1].append(v2)
  nodes[v2].append(v1)

def f(startNode):
  stack = [startNode]
  while stack:
    curNode = stack.pop()
    if visited[curNode] == False:
      visited[curNode] = True
      # 현재 노드가 가리키고있는 다른 노드를 
      # 스택에 추가한다.
      stack += nodes[curNode]

ans = 0
# 정점이 1부터 이므로 1부터 시작 
for i in range(1, N+1):
  if visited[i] == False:
    f(i)
    ans += 1
print(ans)

'''
1)
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
=> 1
2)
6 5
1 2
2 5
5 1
3 4
4 6
=>2
'''