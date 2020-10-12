# 미로찾기 알고리즘에서 다른점은
# 시작 포인트가 여러개다 => 그냥 시작할 때 queue에 여러 포인트를 넣는다.
# 방문 못 하는 노드가 있을 때 예외 처리 => 방문 못 한 노드 있는지 확인
# 끝이 고정이 아니다 => 그냥 순회끝나고 가장 높은 값을 출력한다.


# 생각 1.
# 1. 지도가 들어있는 값 순회 해서 1값을 찾고 찾은 값을 시작때 큐에 넣는다.
# 2. visited에 -1, 못 간 구역 표시가 필요하다.
# 3. 결과 값은 값 순회 한 후 최대거리 값을 출력한다. 또는 길찾기 알고리즘 실행시 판별해서 구함 

w, h = map(int, input().split())
nodes = [0 for _ in range(h)]
for i in range(h):
    nodes[i] = input().split()
visited = [[-1 for _ in range(w)] for _ in range(h)]

def getStartPoints():
    startPoints = []
    for i in range(h):
        for j in range(w):
            if nodes[i][j] == '1':
                startPoints.append([i,j,-1])
            elif nodes[i][j] == '-1':
                visited[i][j] = -2
    return startPoints

def f():
    q = [*getStartPoints()]
    while q:
        y, x, v = q[0]
        del q[0]
        # 범위 벋어나는지 확인
        if y >= 0 and x >= 0 and y < h and x < w:
            node = nodes[y][x] 
            if visited[y][x] == -1 and node != '-1':
                visited[y][x] = v + 1
                q.append([y-1,x, visited[y][x]])
                q.append([y,x+1, visited[y][x]])
                q.append([y+1,x, visited[y][x]])
                q.append([y,x-1, visited[y][x]])

f()
# find max
max = 0
flag = False
for i in range(h):
    for j in range(w):
        if visited[i][j] == -1:
            flag = True
            break
        if max < visited[i][j]:
            max = visited[i][j]
if flag == False:
    print(max)
else:
    print(-1)

