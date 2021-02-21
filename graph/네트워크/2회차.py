'''
'''


def solution(l, computers):
    visited = [False for _ in range(l)]

    def bfs(ni):
        queue = [(computers[ni], ni)]

        while queue:
            computer, ci = queue.pop(0)
            if visited[ci] == False:
                visited[ci] = True
                for i, c in enumerate(computer):
                    if c == 1 and visited[i] == False:
                        queue.append((computers[i], i))

    ans = 0
    for i in range(l):
        if visited[i] == False:
            bfs(i)
            ans += 1
    return ans


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
print(solution(5, [[1, 1, 0, 0, 0], [1, 1, 0, 1, 1], [
      0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 1]]), 2)
print(solution(5, [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [
    0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]), 5)
