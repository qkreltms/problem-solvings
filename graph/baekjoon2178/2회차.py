# 배운 점
'''
1. 재귀를 쓰면 한 곳만 딥하게 파서 최소 거리값을 얻지 못 한다 => stack (DFS)
qeueu를 쓰면 인접한 노드를 우선순위로 간다.

메모리: 29076	속도: 92ms
'''
h, w = list(map(int, input().split()))
arr = [[] for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    arr[i] = list(map(int, input()))


def f():
    stack = [(0, 0, 0)]
    while stack:
        x, y, step = stack.pop(0)
        # x, y가 배열 범위에 속하는지 확인
        if x >= 0 and y >= 0 and x < w and y < h:
            # 해당 좌표값이 방문을  안했는지, 0이 아닌지
            if arr[y][x] and not visited[y][x]:
                visited[y][x] = step + 1
                stack.append([x, y-1, visited[y][x]])
                stack.append([x+1, y, visited[y][x]])
                stack.append([x, y+1, visited[y][x]])
                stack.append([x-1, y, visited[y][x]])


f()
print(visited[h-1][w-1])
