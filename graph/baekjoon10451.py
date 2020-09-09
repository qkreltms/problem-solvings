# 컴포넌트 개수세기 문제
# 포인트: 하나의 노드가 2개 이상을 가리키지 않는다는걸 이용해 1차원 배열으로 속도 문제를 해결할 수 있다.

# 2 몇 번 할지
# 8 순열의 크기
# 3 2 7 8 1 4 5 6 순열
# 10
# 2 1 3 4 5 6 7 9 10 8
# 순열은 중복되는 수가 없는 나열된 수
# 문제를 보면 방향이 있는 그래프이다.
# 이 문제에서는 1->2 2->1 이 될 수는 있어도 1->2, 1->3과 같은 형식은 될 수 없다.

import sys
sys.setrecursionlimit(999999)
def dfs(i):
  if (visit[i] == False):
    visit[i] = True
    dfs(A[i])
  else:
    return

t = int(input())
for _ in range(t):
  n = int(input())
  A = [0] + list(map(int, input().split(" ")))
  visit = [False] * (n + 1)
  
  ans = 0
  for i in range(1, n + 1):
    if visit[i] == False:
      dfs(i)
      ans += 1
  print(ans)

