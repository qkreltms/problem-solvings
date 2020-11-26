# 문제
'''
이분 그래프인지 판별
이분 그래프란? =>
정점을 집합을 둘로 분할하여, 각 집합에 속한 정점끼리 서로 인접x 일 때 이분그래프
'''
# 내 실수
'''
시간초과?!! => sys.stdin.readline()
틀렸다?!! => 1. 인접열이 없는 노드도 순회가 가능해야함
2. 1 - 2, 1 - 3과 같은 구조일 때 1 -> 2, 2 -> 1을 다시 방문할 때
그냥 종료 시켜서 1 -> 3을 가지 않게해야 함

틀렸다?!!
def f(v):
    c = 1
    visited[v] = c
    for s in adj[v]:
        if visited[s] == 0:
            visited[s] = 3 - c
반례:
1
4 3
1 2
3 4
2 4
*한 번에 돌 수 있는 만큼 다 돌아야 한다
왜냐면 1번 부터 n 번 노드 순으로 순회할 때 위의 반례 통과 안됨
'''
# 키 포인트
'''
visited를 이용해 색을 입힌다. 예: c=1, f(3-c)를 재귀적으로 순회해 색을 입힘

n 번째 노드를 선택하고 그 노드와 인접한 정점을 순회할 때 자신과
같은 색이 없다면 이분 그래프

한번 돌 연결된 노드는 다 순회 해야 한다.
'''
# 알게된 것
'''
그래프가 어떤 타입인지 명시 없으면 '무 방향 그래프'
'''




import sys
from collections import deque
def f(v):
    stack = deque([v])
    c = 1
    visited[v] = c
    while stack:
        s = stack.popleft()
        c = visited[s]
        for a in adj[s]:
            if visited[a] != 0:
              if visited[a] == visited[s]:
                  return True
            if visited[a] == 0:
                visited[a] = 3 - c
                stack.append(a)
    return False


t = int(sys.stdin.readline())
for _ in range(t):
    V, E = map(int, sys.stdin.readline().split())
    visited = [0 for _ in range(V+1)]
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        v, e = map(int, sys.stdin.readline().split())
        adj[v].append(e)
        adj[e].append(v)

    for i in range(1, V+1):
        if visited[i] == 0:
            if (f(i)):
                print('NO')
                break
    # break 되면 무시됨
    else:
      print('YES')


'''
# 1.
2
3 2
1 3
2 3
YES
4 4
1 2
2 3
3 4
4 2
NO
# 2
1
999 1
1 1
NO
# 3
1
3 2
1 2
1 3
YES
# 4
1
4 3
1 2
3 4
2 4
'''
