# 문제
'''
컴포넌트 개수구하기랑 같음
'''
# 풀이 법
'''
컴포넌트 개수 구하기 방식 단, 들어오는 값을 그 알고리즘에 맞게 변환한다.
'''


def f(queue):
    global visited
    while queue:
        q = queue.pop(0)
        if visited[q] == False:
            visited[q] = True
            queue += nodes[q]


def solution(n, computers):
    global visited
    global nodes
    visited = [False for _ in range(n)]
    nodes = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                nodes[i].append(j)

    ans = 0
    for i in range(n):
        if visited[i] == False:
            f(nodes[i])
            ans += 1
    return ans


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
print(solution(5, [[1, 1, 0, 0, 0], [1, 1, 0, 1, 1], [
      0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 1]]), 2)
print(solution(5, [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [
    0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]), 5)
