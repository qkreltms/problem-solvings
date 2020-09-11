# 단지번호붙이기
# point: 입력이 2차원 배열, 컴포넌트 개수 세기 문제
# 1)
# 1. 이차원 배열을 왼쪽, 위부터 오른쪽, 아래순으로 순회한다.
# 1. 인자로 i,j, n값이 가야한다.
# 1. 순회 시작전 글로벌 변수로 cnt(단지 안 집 개수), circle(단지 번호), (또는 j로 해도 충분) 변수가 있으며 이 값을 오브젝트 key, value로 관리한다.
# 1. 순회 시작전 cnt = 0으로 초기화 한다.
# 1. i번째(행) j번째(열)로 노드가 방문한 노드인지 체크한다.
# 1. 방문 노드라면 빠져나오고 다음 노드를 순회한다.
# 1. 방믄 노드가 아니라면 계속한다. 
# 1. visited배열을 이용해 방문 노드를 체크한다.
# 1. 노드가 0인지 1인지 확인하다.
# 1. 노드가 0이라면 빠져나오고 다음 노드를 순회한다.
# 1. 노드가 1이라면 4방향 탐색을 시작을 준비한다. 
# 1. cnt 카운트를 시작한다.
# 1. 배열 범위를 벗어났는지 확인한다.
# 1. 범위를 벗어나지 않았으면 카운트를 시작한다.
# 1. 탐색을 시작한다.
# 1. 탐색이 다 끝나면 object를 key 개수만큼 순회하며 정렬하고 출력한다.

# 이 값으로 n * n 행열을 만든다.
import sys
sys.setrecursionlimit(999999)

danjisu = int(input())
nodes = ['0'] * danjisu
visited = [[False for i in range(danjisu)] for i in range(danjisu)]
res = dict()
cnt = 0

# 순회 알고리즘
def f(y, x):
  # 정해진 배열 범위 안인지 확인
  if x >= 0 and y >= 0 and x < danjisu and y < danjisu:
    node = nodes[y][x]
    if visited[y][x] or node == '0':
      return
    visited[y][x] = True
    global cnt
    cnt += 1
    # 4 방향 탐색
    # 위, 오른쪽, 아래, 왼쪽
    # TODO: 배열에 들어가기전 정해진 범위 안인지 확인해야한다.
    f(y - 1, x)
    f(y, x + 1)
    f(y + 1, x)
    f(y, x - 1)
      

for i in range(danjisu):
  nodes[i] = list(input())

for i in range(danjisu):
  for j in range(danjisu):
    cnt = 0
    f(i, j, nodes[i][j])
    # 순회 알고리즘이 종료되면 결과를 기록한다. 
    if cnt != 0:
      res[j] = cnt

for i in sorted(list(res.values())):
  print(i)  


