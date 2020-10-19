# 토마토 알고리즘
# 미로찾기 알고리즘에서 다른점은
# 시작 포인트가 여러개다 => 그냥 시작할 때 queue에 여러 포인트를 넣는다.
# 방문 못 하는 노드가 있을 때 예외 처리 => 방문 못 한 노드 있는지 확인
# 끝이 고정이 아니다 => 그냥 순회끝나고 가장 높은 값을 출력한다.


# 생각 1.
# 1. 지도가 들어있는 값 순회 해서 1값을 찾고 찾은 값을 시작때 큐에 넣는다.
# 2. visited에 -1, 못 간 구역 표시가 필요하다.
# 3. 결과 값은 값 순회 한 후 최대거리 값을 출력한다. 또는 길찾기 알고리즘 실행시 판별해서 구함 

# 생각 2.
# deque를 쓰자. del q[0] 식의 로직보다 속도가 훨씬빠르다.
# 문제를 잘 읽자. "익지 않은 토마토가 하나라도 있는지 확인" 이 로직 추가로 속도 빨라짐
# 예외 케이스를 더 생각해보자... 문제를 다 읽지 않는다고 처도 예외 케이스를 더 잘 생각했으면 처리할 수 있었을지도...?

import sys
from collections import deque
sys.setrecursionlimit(999999)

w, h = map(int, sys.stdin.readline().split())
nodes = [0 for _ in range(h)]
for i in range(h):
    nodes[i] = sys.stdin.readline().split()
visited = [[-1 for _ in range(w)] for _ in range(h)]
# 갈수있는 거리의 길이만 저장할 변수
maxFootprints = w * h
startPoints = []

def f():
    global footPrints
    global maxVisited
    global startPoints
    footPrints = 0
    maxVisited = 0
    q = deque([*startPoints])
    while q:
        y, x, v = q.popleft()
        # 범위 벋어나는지 확인
        if y >= 0 and x >= 0 and y < h and x < w:
            node = nodes[y][x] 
            if visited[y][x] == -1 and node != '-1':
                footPrints += 1
                visited[y][x] = v + 1
                if maxVisited < visited[y][x]:
                    maxVisited = visited[y][x]
                q.append([y-1,x, visited[y][x]])
                q.append([y,x+1, visited[y][x]])
                q.append([y+1,x, visited[y][x]])
                q.append([y,x-1, visited[y][x]])

cnt = 0
startPoints = []
for i in range(h):
    for j in range(w):
        if nodes[i][j] == '1':
            startPoints.append([i,j,-1])
        # 못 가는곳은 길이에서 제외한다.
        elif nodes[i][j] == '-1':
            maxFootprints -= 1
        elif nodes[i][j] == '0':
            cnt += 1
# 익지 않은 토마토가 하나라도 있는지 확인
if cnt <= 0:
    print(0)
else:
    f()
    # 갈수있는 총 0의 개수보다 적개 순회했다? => 못 간 0이 있다. => -1
    if footPrints != maxFootprints:
        print(-1)
    else :
        print(maxVisited)



