# 문제
'''
지도의 m, n 크기, 가지 못하는 영역이 주어질 때
1,1에서 m,n에서 가는 최소 값은?
'''
# 풀이 법
'''
# 1. 미로찾기 BFS알고리즘 사용 => 문제를 잘 보자 최단 경로의 개수!!

# 2. visited 때문에 경로가 다 세어지지 않음

# 3. 시간 초과
'''


class Obj:
    def __init__(self, a):
        self.value = a

    def sum(self, a):
        self.value += a


def solution(w, h, puddles):
    nodes = [[Obj(0) for _ in range(w)] for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for x, y in puddles:
        nodes[y-1][x-1] = Obj(-1)

    queue = [[0, 0, visited[0][0], Obj(1)]]
    while queue:
        y, x, hap, souls = queue.pop(0)
        if y >= 0 and y < h and x >= 0 and x < w:
            if nodes[y][x].value != -1 and visited[h-1][w-1] == 0:
                # 이미 방문했다면
                if visited[y][x] > 0:
                    # 영혼만 보낸다.
                    nodes[y][x].sum(souls.value)
                else:
                    visited[y][x] = hap+1
                    nodes[y][x].value = souls.value
                    queue.append([y, x+1, visited[y][x], nodes[y][x]])
                    queue.append([y+1, x, visited[y][x], nodes[y][x]])

    ans = 0
    if nodes[h-2][w-1].value != -1:
        ans += nodes[h-2][w-1].value
    if nodes[h-1][w-2].value != -1:
        ans += nodes[h-1][w-2].value
    return ans % 1000000007


print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(3, 3, [[2, 2]]), 2)
print(solution(3, 3, [[2, 3]]), 3)
print(solution(3, 3, [[1, 3]]), 5)
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(solution(1, 2, []), 1)
print(solution(2, 1, []), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [
      4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
print(solution(4, 4, [[3, 2], [2, 4]]), 7)
print(solution(100, 100, []), 690285631)
