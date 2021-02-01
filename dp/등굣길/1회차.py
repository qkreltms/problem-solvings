# 문제
'''
지도의 m, n 크기, 가지 못하는 영역이 주어질 때
1,1에서 m,n에서 가는 최소 값은?
'''
# 풀이 법
'''
# 1. BFS알고리즘 사용 => 문제를 잘 보자 최단 경로의 개수!!

# 2. visited 때문에 경로가 다 세어지지 않음

# 3. 시간 초과
'''


def solution(w, h, puddles):
    nodes = [[0 for _ in range(w)] for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for x, y in puddles:
        nodes[y-1][x-1] = 1

    queue = [[0, 0, visited[0][0]]]
    ans = 0
    while queue:
        y, x, hap = queue.pop(0)
        if y >= 0 and y < h and x >= 0 and x < w:
            if nodes[y][x] != 1 and visited[h-1][w-1] == 0:
                visited[y][x] = hap+1
                queue.append([y+1, x, visited[y][x]])
                queue.append([y, x+1, visited[y][x]])
            if y == h-1 and x == w-1 and hap+1 == visited[h-1][w-1]:
                ans += 1

    return ans % 1000000007


print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(3, 3, [[2, 2]]), 2)
# print(solution(1, 2, []), 0)
# print(solution(4, 3, [[2, 2]]), 4)
# print(solution(4, 3, [[2, 2], [3, 3]]), 4)
# print(solution(5, 4, [[2, 2], [3, 3], [4, 4], [4, 1], [5, 2]]), 6)
